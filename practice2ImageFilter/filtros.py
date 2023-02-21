import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("building-windows.jpg", cv2.IMREAD_UNCHANGED)
img_gray = cv2.imread("building-windows.jpg", cv2.IMREAD_GRAYSCALE)
retval, img_tresh = cv2.treshgold(img_gray, 100, 255, cv2.TRESH_BINARY)

img_reverso = img[:,:,::-1] #Invierte los colores de BGR a RGB

matrix3 = (30,30)
matrix1 = np.ones(img_reverso.shape) * .6
matrix2 = np.ones(img_reverso.shape) * 1.5
#img_shdw = np.uint8(cv2.multiply(np.float64(img_reverso), matrix1))
#img_white = np.uint16(cv2.multiply(np.float64(img_reverso), matrix2))
img_blur = cv2.blur(img_reverso, matrix3)

plt.figure(figsize=[10, 5])
plt.subplot(221);plt.imshow(img_reverso);plt.title("Casona RGB");
plt.subplot(222);plt.imshow(img_blur);plt.title("Casona borrosona");
plt.subplot(223);plt.imshow(img_gray, cmap="gray");plt.title("Casona grisona");
plt.subplot(224);plt.imshow(img_tresh, cmap="gray");plt.title("Casona tresheadas");
plt.show()