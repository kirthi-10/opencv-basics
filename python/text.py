
import numpy as np
import cv2 as cv

# blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)
#paint the blank image
#blank[:]=0,0,255
#cv.imshow('green',blank)

#draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)
# cv.imshow('rectangle',blank)

# cv.putText(blank,'hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
# cv.imshow('text',blank)

img=cv.imread('greencheek.jpg')
cv.imshow('image',img)

#resizing the image
resize = cv.resize(img, (500,550))
cv.imshow("Resized Image", resize)


text=cv.putText(resize,'open cv beginner',(50,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv.imshow('Text',text)

cv.waitKey(0)