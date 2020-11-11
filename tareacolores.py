import cv2
import numpy as np

img=cv2.imread('rojo.jpg')
img2=cv2.imread('marron.jpg')
img3=cv2.imread('celeste.jpg')

hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv2=cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
hsv3=cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

rojo_bajo=np.array([0,100,20])
rojo_alto=np.array([8,255,255])

marron_bajo=np.array([10,5,5])
marron_alto=np.array([71,209,127])

celeste_bajo=np.array([50,120,200])
celeste_alto=np.array([255,255,255])

mask=cv2.inRange(hsv,rojo_bajo,rojo_alto)
mask2=cv2.inRange(hsv2,marron_bajo,marron_alto)
mask3=cv2.inRange(hsv3,celeste_bajo,celeste_alto)

cv2.imshow('foto original',img)
cv2.imshow('foto rojo',mask)
cv2.imshow('foto original 2',img2)
cv2.imshow('foto marron',mask2)
cv2.imshow('foto original 3',img3)
cv2.imshow('foto celeste',mask3)

cv2.destroyALLWindows()
