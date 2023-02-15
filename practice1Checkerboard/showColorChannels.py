import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Tigre.jpg", cv2.IMREAD_COLOR)
cv2.imshow('H channel', img[:, :, 0])
cv2.imshow('S channel', img[:, :, 1])
cv2.imshow('V channel', img[:, :, 2])
