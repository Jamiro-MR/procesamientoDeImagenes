#Gutierrez Bejarano Braulio Roberto - 4D
import cv2
import numpy as np
video = cv2.VideoCapture(0) #Inicia captura de video

#Error de camara
if (video.isOpened()== False):
	print("Error al abrir la camara.")
flag = 0

#Se abre video
while(video.isOpened()): 
	ret, frame = video.read() #Frames
	if ret == True:
		k = cv2.waitKey(1)
		if k == 103: #Tecla G para gris
			frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
		elif k == 121: #Tecla Y para gama YUV
			frame = cv2.cvtColor(frame, cv2.COLOR_RGB2YUV)
		elif k == 104: #Tecla H parq gama HSV
			frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
		cv2.imshow('Video chistoson: Imagenes reales de un nahual', frame)
		if k == 113 or k == 120: #Teclas de exit
			break
	else:
		break
video.release()
cv2.destroyAllWindows() #Destruye todas las ventanas