import cv2

image = cv2.imread(r'C:/Users\nisarg prajapati\OneDrive\Documents\Downloads\360p-resolution.jpg')
blur = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
