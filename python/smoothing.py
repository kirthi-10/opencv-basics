import cv2 as cv
import numpy as np


img=cv.imread('people img.webp')
cv.imshow('people',img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
resized_image=rescaleFrame(img)
cv.imshow('image',resized_image)

#blurring techniques
#averaging 
average=cv.blur(resized_image,(3,3))
cv.imshow('Average',average)


#gaussian blur
gauss=cv.GaussianBlur(resized_image,(3,3),0)
cv.imshow('blur',gauss)

#median blur
median=cv.medianBlur(resized_image,3)
cv.imshow('Median',median)

#bilateral filter
bilateral=cv.bilateralFilter(img,10,15,15)
cv.imshow('bilateral',bilateral)


cv.waitKey(0)






cv.waitKey(0)
