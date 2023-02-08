import cv2

img = cv2.imread('Tigre.jpg', cv2.IMREAD_UNCHANGED)
cv2.imwrite("Tigrito.jpg", img)
cv2.imshow("La imagen procesada mas malota", img)

img2 = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Mi compa toño tumbao", img2)

#Un rectangulo largote
#cv2.rectangle(img,(0, 28),(84,56),(0,0,0),-1)

#2 rectangulos
#cv2.rectangle(img,(0, 28),(28,56),(0,0,255),-1)
#cv2.rectangle(img,(55, 28), (84, 56), (0,0,255),-1)

#Letra I
#cv2.rectangle(img,(27, 0), (55, 28), (0,0,0),-1)
#cv2.rectangle(img,(27, 56), (56, 84), (0,0,0),-1)

#Funciones
#print(img)
print(img.shape)
print(type(img))
print(img.size)

print(img[0,42])
print(cv2.__version__)
cv2.waitKey(0)