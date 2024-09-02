
# Python program to illustrate  
# arithmetic operation of 
# subtraction of pixels of two images

import cv2  as cv
import numpy as np

img1=cv.imread('pic5.jpeg')
img2=cv.imread('pic4.png')

new_width,new_height=400,300

resized_img1=cv.resize(img1,(new_width,new_height))
resized_img2=cv.resize(img2,(new_width,new_height))

cv.imshow('pic1',resized_img1)
cv.imshow('pic2',resized_img2)


sub=cv.subtract(resized_img1,resized_img2)
cv.imshow('subtracted_img',sub)


cv.waitKey(0)
cv.destroyAllWindows()