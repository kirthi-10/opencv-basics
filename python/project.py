import cv2 as cv
import numpy as np

img=cv.imread('im.webp')
cv.imshow('img',img)

# represents the top left corner of rectangle 
start_point =(100,150)

# represents the bottom right corner of rectangle 
end_point = (300, 350) 

# Blue color in BGR 
color = (255, 0, 0)

# Line thickness of 2 px 
thickness = 2

# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image=cv.rectangle(img,start_point ,end_point,color ,thickness)

cv.imshow('window',image)

# Center coordinates 
center_coordinates = (500,420) 

# Radius of circle 
radius = 100

# Blue color in BGR 
color = (0,0,255) 
   
# Line thickness of 2 px 
thickness = 2
   
# Using cv2.circle() method 
# Draw a circle with blue line borders of thickness of 2 px
image=cv.circle(img,center_coordinates,radius,color ,thickness)


cv.imshow('window',image)

cv.waitKey(0)
cv.destroyAllWindows()