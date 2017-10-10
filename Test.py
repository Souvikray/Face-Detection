import cv2
import numpy as np
from skimage.measure import compare_ssim

def ssim(A, B):
    return compare_ssim(A, B, data_range=A.max() - A.min())


def mse(A, B):
    return ((A - B) ** 2).mean()


cap = cv2.VideoCapture('Sample Video.webm')
# cap = cv2.VideoCapture(0)

curr_frame = None
prev_frame = None
first_frame = True

while True:
    prev_frame = curr_frame
    _, curr_frame = cap.read()
    if curr_frame is None:
        break

    curr_frame = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
    if first_frame:
        prev_frame = curr_frame
        first_frame = False

    #cv2.imshow('app', curr_frame)
    print(ssim(curr_frame, prev_frame))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
