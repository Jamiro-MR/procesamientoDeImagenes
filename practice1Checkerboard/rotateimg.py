import cv2
import numpy

img = cv2.imread("Tigre.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("Mexico desperto", img)

num_rows, num_cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), -45, 1)
img2 = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
cv2.imshow("EL tigre mas rotado", img2)

cv2.waitKey(0)