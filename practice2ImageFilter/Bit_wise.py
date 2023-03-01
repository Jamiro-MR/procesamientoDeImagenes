import cv2
import matplotlib.pyplot as plt

img_rec = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
img_circ = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)
Tigre = cv2.imread("Tigre.jpg", cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=[20,5])
plt.subplot(121);plt.imshow(img_rec, cmap="gray");plt.title("Rectangulo");
plt.subplot(122);plt.imshow(img_circ, cmap="gray");plt.title("Circulo");
plt.show()

img_bitwise = cv2.bitwise_not(Tigre, mask=None)
plt.imshow(img_bitwise, cmap="gray")
plt.show()