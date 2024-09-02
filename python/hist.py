# import Opencv 
import cv2 
  
# import Numpy 
import numpy as np 
  
# read a image using imread 
img = cv2.imread('im1.jpeg') 

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  
# creating a Histograms Equalization 
# of a image using cv2.equalizeHist() 
equ = cv2.equalizeHist(img_gray) 

equ = cv2.resize(equ, (img_gray.shape[1], img_gray.shape[0]))
  
# stacking images side-by-side 
res = np.hstack((img, equ)) 
  
# show image input vs output 
cv2.imshow('window',res) 
  
cv2.waitKey(0) 
cv2.destroyAllWindows() 