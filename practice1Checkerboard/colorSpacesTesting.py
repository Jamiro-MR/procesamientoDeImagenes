import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Tigre.jpg", cv2.IMREAD_UNCHANGED)
img_reverso = img[:,:,::-1] #Invierte los colores de BGR a RGB

#Conversión a YUV
img_yuv = cv2.cvtColor(img_reverso, cv2.COLOR_BGR2YUV)
#plt.imshow(img_yuv)

#Conversión a HSV
img_hsv = cv2.cvtColor(img_reverso, cv2.COLOR_BGR2HSV)
#plt.imshow(img_hsv)

#Conversión a YCrCb
img_YCrCb = cv2.cvtColor(img_reverso, cv2.COLOR_BGR2YCrCb)

plt.figure(figsize=[10, 5])

plt.subplot(221);plt.imshow(img_reverso);plt.title("Tigre toño RGBeado");
plt.subplot(222);plt.imshow(img_YCrCb);plt.title("Tigre toño formato curioson");
plt.subplot(223);plt.imshow(img);plt.title("Tigre toño");
plt.subplot(224);plt.imshow(img_yuv);plt.title("Tigre toño yuveado");

#plt.imshow(img_ycrcb)
#plt.title('Tigre toño yuveado')
plt.show()