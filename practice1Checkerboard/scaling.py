import cv2
import numpy as np

img = cv2.imread("Tigre.jpg")
cv2.imshow("Tigre despiertado", img)

img2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("tigrito", img2)
cv2.waitKey(0)