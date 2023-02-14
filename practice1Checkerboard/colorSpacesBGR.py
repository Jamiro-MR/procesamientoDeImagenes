import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Tigre.jpg", cv2.IMREAD_COLOR)
img_reverso = img[:,:,::-1]
img_yuv = cv2.cvtColor(img_reverso, cv2.COLOR_BGR2HSV)
plt.imshow(img_yuv)
plt.title('Tigre toño yuveado')
plt.show()