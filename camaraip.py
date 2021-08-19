#!C:\Users\alvar\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
#
# camaraip.py
#
# Creado: 06/08/2021
# Versión: 001
# Ultima modificación:
#
# Copyright 2019 Alvaro Alejandro Guiffrey <alvaroguiffrey@gmail.com>
#

# Modulos que se importan de la librería estandar

import numpy as np
import cv2

cap = cv2.VideoCapture('http://admin:admin@192.168.0.73:8081/video')

while(True):

    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    #if cv2.waitKey(1) & 0xFF == ord('q'): # utiliza una tecla según lo que ponés
    if cv2.waitKey(1) & 0xFF == 27: # utiliza la tecla 'esc'
        break

cap.release()
cv2.destroyAllWindows()
