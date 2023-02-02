import cv2

img = cv2.imread('checkerboard.jpg')

cv2.imshow("La imagen precesada mas malota", img)

cv2.waitKey(0)

print(cv2.__version__)