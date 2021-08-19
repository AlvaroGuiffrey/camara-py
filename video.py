#!C:\Users\alvar\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
#
# video.py
#
# Creado: 02/08/2021
# Versión: 001
# Ultima modificación:
#
# Autor: Gaby https://www.youtube.com/watch?v=RLpXUP79U2Y
# Copyright 2019 Alvaro Alejandro Guiffrey <alvaroguiffrey@gmail.com>
#

# Modulos que se importan de la librería estandar
import cv2

# Constantes para fecha


# Captura imagen desde la cámara de la pc
#captura = cv2.VideoCapture(0)
# Captura video cámara del sansumg
captura = cv2.VideoCapture('http://admin:admin@192.168.0.73:8081/video')
# Captura video cámara tablet gadnic
#captura = cv2.VideoCapture('http://alvaritz:monoloco@192.168.0.106:8081/video')
# Toma el video guardado
#captura = cv2.VideoCapture('videoPrueba.avi')
# Salida de la imagen capturada para guardar
# En formate AVI
#salida = cv2.VideoWriter('videoPrueba.avi', cv2.VideoWriter_fourcc(*'XVID'),
#                            20.0, (640,480))
# En formato MP4
salida = cv2.VideoWriter('videoPrueba.mp4', cv2.VideoWriter_fourcc(*'MP4V'),
                            20.0, (640,480))

while (captura.isOpened()):
    ret, imagen = captura.read()
    if ret==True:
        cv2.imshow('video',imagen)
        cv2.moveWindow('video', 100, 100) # posición del cuadro
        salida.write(imagen)
        #if cv2.waitKey(1) & 0xFF == ord('s'):
        # Sale con tecla "esc"
        if cv2.waitKey(1) & 0xFF == 27:
            break
captura.release()
salida.release()
cv2.destroyAllWindows()
