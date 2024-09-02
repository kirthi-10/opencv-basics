
import cv2 as cv
import numpy as np

img=cv.imread('people img.webp')
cv.imshow('image',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)


print(img.shape)
print(blue.shape)
print(green.shape)
print(red.shape)

merged=cv.merge([b,g,r])
cv.imshow('merged image',merged)
cv.waitKey(0)