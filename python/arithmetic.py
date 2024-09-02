import cv2 as cv
import numpy as np

# path to input images are specified and   
# images are loaded with imread command  
image1 = cv.imread('pic1.jpg')  
image2 = cv.imread('pic2.jpeg') 


new_width = 400
new_height = 300

# Resize the images
resized_image1 = cv.resize(image1, (new_width, new_height))
resized_image2 = cv.resize(image2, (new_width, new_height))

# Display the resized images
cv.imshow('Resized Image 1', resized_image1)
cv.imshow('Resized Image 2', resized_image2)

weightedsum= cv.addWeighted(resized_image1,0.4,resized_image2,0.5,0)
cv.imshow('weighted image',weightedsum)

cv.waitKey(0)
cv.destroyAllWindows()

