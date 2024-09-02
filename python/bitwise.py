import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

top_left = (50, 50)
bottom_right = (300, 300)
color = (0, 255, 0)  # Color in BGR format (here, green)


rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,150),100,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise and
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise and',bitwise_and)

#bitwise or
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise or',bitwise_or)

#bitwise xor
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise or',bitwise_xor)

#bitwise not
bitwise_not=cv.bitwise_not(circle)
cv.imshow('bitwise not',bitwise_not)

cv.waitKey(0)
