import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Tigre.jpg", cv2.IMREAD_COLOR)
img_reverso = img[:,:,::-1] #Invierte los colores de BGR a RGB

#Conversión a YUV
#img_yuv = cv2.cvtColor(img_reverso, cv2.COLOR_BGR2YUV)
#plt.imshow(img_yuv)

#Conversión a HSV
#img_hsv = cv2.cvtColor(img_reverso, cv2.COLOR_BGR2HSV)
#plt.imshow(img_hsv)

#Conversión a YCrCb
img_ycrcb = cv2.cvtColor(img_reverso, cv2.COLOR_RGB2YCrCb)
plt.figure(figsize=[10, 5])
plt.subplot(11);plt.imshow(img_reverso);plt.title("Tigre toño rgbeado");
plt.subplot(12);plt.imshow(img_ycrcb);plt.tittle("Tigre en el formato chistoso");

#plt.imshow(img_ycrcb)
#plt.title('Tigre toño yuveado')
plt.show()