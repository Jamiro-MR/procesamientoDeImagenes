import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('Monumento.jpg')

img_blur = cv2.blur(img, (15,15))
img_median = cv2.medianBlur(img,5)
img_gauss = cv2.GaussianBlur(img,(5,5),0)
img_bilateral = cv2.bilateralFilter(img,9,75,75)
img_laplaciano = cv2.Laplacian(img_gauss, cv2.CV_64F)
img_laplaciano_b = img_laplaciano/img_laplaciano.max()

plt.figure(figsize=[20,5])
plt.subplot(431);plt.imshow(img);plt.title("Edificio");
plt.subplot(432);plt.imshow(img_blur);plt.title("Edificio blurreado");
plt.subplot(433);plt.imshow(img_gauss);plt.title("Edificio gauseado");
plt.subplot(434);plt.imshow(img_median);plt.title("Edificio medianano");
plt.subplot(435);plt.imshow(img_bilateral);plt.title("Edificio bicurioso");
plt.subplot(436);plt.imshow(img_laplaciano);plt.title("Edificio laplaceado");
plt.subplot(437);plt.imshow(img_laplaciano_b);plt.title("Edificio laplaceado B SIDE");

plt.show()