from email.mime import image

import cv2
import numpy as np
image = cv2.imread('C:/Users/nisarg prajapati/OneDrive/Documents/Downloads/360p-resolution.jpg', cv2.IMREAD_GRAYSCALE)
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100
params.maxArea = 5000
params.filterByCircularity = True
params.minCircularity = 0.8
params.filterByConvexity = True
params.minConvexity = 0.7
params.filterByInertia = True
params.minInertiaRatio = 0.5
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(image)
output_image = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Blob Detection', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
