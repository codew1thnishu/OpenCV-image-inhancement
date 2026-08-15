# OpenCV-image-inhancement
import cv2
import numpy as np

image = cv2.imread('C:/Users/nisarg prajapati/OneDrive/Documents/Downloads/360p-resolution.jpg')

bright = cv2.convertScaleAbs(image, alpha=1.2, beta=30)

cv2.imshow('Original Image', image)
cv2.imshow('Bright Image', bright)

cv2.waitKey(0)
cv2.destroyAllWindows()



