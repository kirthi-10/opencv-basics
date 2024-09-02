
import numpy as np
import cv2 as cv

img=cv.imread('job.webp')
cv.imshow('pic',img)

#grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

#bluring the image
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#edgecascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)

#ret threshold function in case of the canny edgescale
#ret,thresh=cv.threshold(gray,125,175,cv.THRESH_BINARY)
#cv.imshow('Thresh',thresh)

#find contours method
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('contours drawn',blank)


cv.waitKey(0)