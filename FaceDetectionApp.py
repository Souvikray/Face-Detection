import cv2
import numpy as np

#capture a video either from a file or a live video stream
cap = cv2.VideoCapture("Sample Video.webm")
#cap = cv2.VideoCapture(0)
while True:
    #get a frame from the video
    ret, frame = cap.read()
    #if we reach the end of the video in case of a video file,stop reading
    if frame is None:
        break

    #show the video as a series of frames
    cv2.imshow("Object Detection",frame) #(name of the window,image file)

    key = cv2.waitKey(1) & 0xFF  #cv2.waitKey(1) returns a value of -1 which is masked using & 0xFF to get char value
    if key == ord('q'): #gives ASCII value of 'q'
        break

#release the resources allocated to the video file or video stream
cap.release()
#destroy all the windows
cv2.destroyAllWindows()

