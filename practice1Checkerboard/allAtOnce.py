import cv2
import numpy as np

img = cv2.imread("Tigre.jpg")

num_rows, num_cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), -45, 1)
translation_matrix = np.float32([[-1, 0, 960], [0, 1, 0]])

img = cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Tigre despiertado", img)
cv2.waitKey(0)
cv2.imwrite("Todas las transformaciones de goku.jpg", img)