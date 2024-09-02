import cv2 as cv
import numpy as np

img=cv.imread('greencheek.jpg')
cv.imshow('cheek',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,255,-1)
cv.imshow('mask',mask)

masking=cv.bitwise_and(img,img,mask=mask)
cv.imshow('mask img',masking)
cv.waitKey(0)