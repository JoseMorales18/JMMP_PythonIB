import cv2
import numpy as np

img=cv2.imread("CirculoColores.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

azul_bajos=np.array([100,50,50])
azul_altos=np.array([130,255,255])

amarillo_bajos=np.array([20,100,20])
amarillo_altos=np.array([32,255,255])

verde_bajos=np.array([36,100,20])
verde_altos=np.array([90,255,255])

rojo_bajos=np.array([0,100,20])
rojo_altos=np.array([10,255,255])

violeta_bajos=np.array([146,100,20])
violeta_altos=np.array([170,255,255])

mask_azul=cv2.inRange(hsv,azul_bajos,azul_altos)
mask_amarillo=cv2.inRange(hsv,amarillo_bajos,amarillo_altos)
mask_verde=cv2.inRange(hsv,verde_bajos,verde_altos)
mask_rojo=cv2.inRange(hsv,rojo_bajos,rojo_altos)
mask_violeta=cv2.inRange(hsv,violeta_bajos,violeta_altos)
mask_union=cv2.bitwise_or(mask_azul,mask_verde)
mask_union2=cv2.bitwise_or(mask_amarillo,mask_rojo)
mask_union12=cv2.bitwise_or(mask_union,mask_union2)
mask_unionT=cv2.bitwise_or(mask_union12,mask_violeta)


cv2.imshow("Original",img)
cv2.imshow("Todos-Naranja",mask_unionT)

print("nPulsa cualquier tecla para cerrar")
cv2.waitKey(0)
