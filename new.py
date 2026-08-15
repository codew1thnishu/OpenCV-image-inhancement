import cv2
import numpy as np
from matplotlib import image
immage = cv2.imread(r'C:\Users\nisarg prajapati\OneDrive\Documents\Downloads\360p-resolution.jpg')
gray = cv2.cvtColor(immage, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

corners = cv2.cornerHarris(gray, 2, 3, 0.04)

image[corners > 0.01 * corners.max()] = [0, 0, 255]

cv2.imshow('Corners Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
 

