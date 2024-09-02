import cv2 as cv

img=cv.imread('cat img.webp')
cv.imshow('cat',img)

#rescaling the image
def rescaleFrame(frame,scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
resized_image=rescaleFrame(img)
cv.imshow('image',resized_image)

#converting into grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


#converting the image into blur

blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur) 


#edge cascade

img2=cv.imread('people img.webp')
cv.imshow('imge',img2)

canny=cv.Canny(img2,125,175)
cv.imshow('Cannyedges',canny)

#dilated image
dilated=cv.dilate(canny,(4,4),iterations=3)
cv.imshow('Dilated',dilated)


#converting into eroded img
eroded=cv.erode(dilated,(3,3),iterations=2)
cv.imshow('erode',eroded)

#resize the img
resized=cv.resize(img2,(500,500))
cv.imshow('Resized',resized)


#cropping the img using array slicing

cropping=img2[50:200,200:400]
cv.imshow('crop',cropping)
cv.waitKey(0)