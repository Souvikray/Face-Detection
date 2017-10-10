import cv2
import numpy as np
from skimage.measure import compare_ssim

#we can compare two images using Structural Similarity
#so a small change in pixel value won't prompt this method to term both images as dissimilar
#the closer the value is to 1,the more similar two images are
def ssim(A, B):
    return compare_ssim(A, B, data_range=A.max() - A.min())

#we can compare two images using Mean Square method
#any change in pixel value will prompt this method to term both images as dissimilar
#result lies between 0 and higher number
def mse(A, B):
    return ((A - B) ** 2).mean()

#capture a video either from a file or a live video stream
cap = cv2.VideoCapture("Sample Video.webm")
#cap = cv2.VideoCapture(0)
first_frame = True
prev_frame = None
current_frame = None
frame_counter = 0
while True:
    if frame_counter == 0:
        #prev_frame will always trail behind the current_frame
        prev_frame = current_frame
    #get a frame from the video
    ret, current_frame = cap.read()
    #if we reach the end of the video in case of a video file,stop reading
    if current_frame is None:
        break

    #convert the image to grayscale
    current_frame = cv2.cvtColor(current_frame,cv2.COLOR_BGR2GRAY)
    if first_frame:
        #for the first time prev_frame and current_frame will be the same
        prev_frame = current_frame
        first_frame = False

    #the idea is instead of comparing two consecutive frames,we compare frames that are 10 intervals apart.
    #This will take care that if there is change in the video but its rate of change is too slow,then it can't pickup
    #the change if we compare consecutive frames.Also the difference between the frames shouldn't be at very high intervals
    #such that if there is a quick change in the video,it can't detect it.So we set a difference in time interval
    #between two frames at 10
    #this also ensures that the SSIM calculation is not too slow
    if frame_counter == 9:
        #compare two images based on SSIM
        print(ssim(current_frame, prev_frame))

        #compare two images based on MSM
        #print(mse(current_frame, prev_frame))

        frame_counter = -1

    #show the video as a series of frames
    cv2.imshow("Object Detection",current_frame) #(name of the window,image file)
    frame_counter += 1

    key = cv2.waitKey(1) & 0xFF  #cv2.waitKey(1) returns a value of -1 which is masked using & 0xFF to get char value
    if key == ord('q'): #gives ASCII value of 'q'
        break

#release the resources allocated to the video file or video stream
cap.release()
#destroy all the windows
cv2.destroyAllWindows()

