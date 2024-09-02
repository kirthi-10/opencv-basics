import cv2 as cv
import numpy as np

# Creating a VideoCapture object to read the video
cap = cv.VideoCapture('video.mp4')
 
 
# Loop until the end of the video
while (cap.isOpened()):
 
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv.resize(frame, (540, 380), fx = 0, fy = 0,
                         interpolation = cv.INTER_CUBIC)
 
    # Display the resulting frame
    cv.imshow('Frame', frame)
 
    # conversion of BGR to grayscale is necessary to apply this operation
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
    # adaptive thresholding to use different threshold 
    # values on different regions of the frame.
    Thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                           cv.THRESH_BINARY_INV, 11, 2)
 
    cv.imshow('Thresh', Thresh)
    # define q as the exit button
    if cv.waitKey(25) & 0xFF == ord('q'):
        break
 
# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv.destroyAllWindows()