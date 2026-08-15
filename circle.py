import cv2
import numpy as np

image = cv2.imread(r'C:\Users\nisarg prajapati\OneDrive\Documents\Downloads\360p-resolution.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,20, param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
