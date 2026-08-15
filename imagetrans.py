import cv2
import numpy as np

image = cv2.imread('C:/Users/nisarg prajapati/OneDrive/Documents/Downloads/360p-resolution.jpg')

rows , cols = image.shape[:2]
matrix = cv2.getRotationMatrix2D((cols/2,rows/2),480,1)
rotated =cv2.warpAffine(image,matrix,(cols,rows))
cv2.imshow('origional image',image)
cv2.imshow('rotated image',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()