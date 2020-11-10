"Detectar Colores José Morales"
 
import cv2
import numpy as np
 
captura = cv2.VideoCapture(0)
 
while(1):
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    azul_bajos = np.array([100,50,50], dtype=np.uint8)
    azul_altos = np.array([130, 255, 255], dtype=np.uint8)
    amarillo_bajos=np.array([20,100,20],dtype=np.uint8)
    amarillo_altos=np.array([32,255,255],dtype=np.uint8)
    rojo_bajos=np.array([0,100,20],dtype=np.uint8)
    rojo_altos=np.array([10,255,255],dtype=np.uint8)
    
    mask_azul=cv2.inRange(hsv,azul_bajos,azul_altos)
    mask_amarillo=cv2.inRange(hsv,amarillo_bajos,amarillo_altos)
    mask_rojo=cv2.inRange(hsv,rojo_bajos,rojo_altos)
    mask_union=cv2.bitwise_or(mask_azul,mask_amarillo)
    mask_union2=cv2.bitwise_or(mask_union,mask_rojo)
 
    moments = cv2.moments(mask_union2)
    area = moments['m00']
 
    if(area > 2000000):
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
        print ("x = ", x)
        print ("y = ", y)
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)
     
    cv2.imshow('mask', mask_union2)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()
