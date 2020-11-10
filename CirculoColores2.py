import cv2
import numpy as np

img=cv2.imread("CirculoColores.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

verde_bajos=np.array([36,100,20])
verde_altos=np.array([90,255,255])

violeta_bajos=np.array([146,100,20])
violeta_altos=np.array([170,255,255])

naranja_bajos=np.array([11,100,20])
naranja_altos=np.array([19,255,255])

mask_verde=cv2.inRange(hsv,verde_bajos,verde_altos)
mask_naranja=cv2.inRange(hsv,naranja_bajos,naranja_altos)
mask_violeta=cv2.inRange(hsv,violeta_bajos,violeta_altos)

mask_union=cv2.bitwise_or(mask_naranja,mask_verde)
mask_unionT=cv2.bitwise_or(mask_union,mask_violeta)

cv2.imshow("Original",img)
cv2.imshow("Verde+Naranja+Violeta",mask_unionT)

print("nPulsa cualquier tecla para cerrar")
cv2.waitKey(0)
