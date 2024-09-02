
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('people img.webp')
cv.imshow('image',img)

#plt.imshow(img)
#plt.show()

#grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV (HUE SATURATION VALUE)
HSV=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',HSV)

#BGR to LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('Lab',lab)

#BGR to rgb
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)


#inversions of the images lab to bgr 
lab_bgr=cv.cvtColor(lab,cv.COLOR_Lab2BGR)
cv.imshow('Lab-->Bgr',lab_bgr)

#hsv to bgr
hsv_bgr=cv.cvtColor(HSV,cv.COLOR_HSV2BGR)
cv.imshow('hsv-->bgr',hsv_bgr)




cv.waitKey(0)