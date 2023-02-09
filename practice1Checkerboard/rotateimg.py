import cv2
import numpy as np

img = cv2.imread("Tigre.jpg")

cv2.imshow("Tigre despiertado", img)

num_rows, num_cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), -45, 1)
translation_matrix = np.float32([[-1, 0, 960], [0, 1, 0]])

img2 = cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))
#img2 = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))

cv2.imshow("tigre volteado", img2)

cv2.waitKey(0)