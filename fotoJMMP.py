import cv2
import tkinter 
import Image,ImageTk
from tkinter import *

root=tkinter.Tk()
root.title('Foto')
root.geometry('620x375')

def otra():
    start()
def start():
    camara= cv2.VideoCapture(0)
    leido,frame=camara.read()
    if leido==True:
        cv2.imwrite('JoseMiguelMoralesPonce.png',frame)
        print('se tomo la foto con exito')
    else:
        print('Error Camara no existe o esta apagada')
        camara.release()
    foto=PhotoImage(file='JoseMiguelMoralesPonce.png')
    fondo=Label(root,image=foto).place(x=0,y=0)
    texto=StringVar()
    texto.set("¿OTRA FOTO?")
    eti=Label(root,textvariable=texto).place(x=510,y=280)
    boton=Button(root,text='SI',command=otra).place(x=500,y=310)
    boton2=Button(root,text='NO',command=root.destroy).place(x=560,y=310)
    
    root.mainloop()
start()
input(" ")

    


