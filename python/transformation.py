import cv2 as cv
import numpy as np
img=cv.imread('people img.webp')
cv.imshow('image',img)

#translation
def translate(img,x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)
# -x --> left
# -y --> up
# x --> right
# y --> down

translated=translate(img,100,-100)
cv.imshow('Translated',translated)


#rotation of image

def rotate(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]

    if rotpoint is None:
        rotpoint= (width//2 ,height//2)
    rotmat=cv.getRotationMatrix2D(rotpoint,angle,1.0)

    dimensions=(width,height)
    return cv.warpAffine(img,rotmat,dimensions)

rotated=rotate(img,-45)
cv.imshow('Rotated',rotated)

rotated_rotated=rotate(rotated,-45)
cv.imshow('Rotate_Rotate',rotated_rotated)


#resized the image

resized=cv.resize(rotated,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)


#flipping the image

flipp=cv.flip(img,0)
cv.imshow('Flipping',flipp)

# cropping the image

cropped=img[200:400,300:500]
cv.imshow("cropped",cropped)
cv.waitKey(0)