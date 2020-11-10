"Menu de Estados casos Covid"


import json
from tkinter import *
from tkinter.ttk import *

ags={}
ags['Casos']=[]
ags['Casos'].append({
    'Confirmados':7270,'Negativos':14407,
    'Sospechosos':915,'Defunciones':630,
    'Recuperados':5043,'Activos':301
    })
BC={}
BC['Casos']=[]
BC['Casos'].append({
    'Confirmados':19510,'Negativos':12040,
    'Sospechosos':1612,'Defunciones':3586,
    'Recuperados':12482,'Activos':298
    })
BCS={}
BCS['Casos']=[]
BCS['Casos'].append({
    'Confirmados':10341,'Negativos':14113,
    'Sospechosos':516,'Defunciones':469,
    'Recuperados':8461,'Activos':641
    })
Camp={}
Camp['Casos']=[]
Camp['Casos'].append({
    'Confirmados':5982,'Negativos':7043,
    'Sospechosos':142,'Defunciones':820,
    'Recuperados':4014,'Activos':55
    })
Chis={}
Chis['Casos']=[]
Chis['Casos'].append({
    'Confirmados':6552,'Negativos':5209,
    'Sospechosos':211,'Defunciones':1090,
    'Recuperados':4039,'Activos':51
    })
QR={}
QR['Casos']=[]
QR['Casos'].append({
    'Confirmados':11759,
    'Negativos':7921,
    'Sospechosos':671,
    'Activos':347,
    'Recuperados':7943,
    'Fallecidos':1640
    })
SLP={}
SLP['Casos']=[]
SLP['Casos'].append({
    'Confirmados':22910,
    'Negativos':27386,
    'Sospechosos':1739,
    'Activos':637,
    'Recuperados':28585,
    'Fallecidos':1664
    })
SIN={}
SIN['Casos']=[]
SIN['Casos'].append({
    'Confirmados':1815,
    'Negativos':14464,
    'Sospechosos':1260,
    'Activos':364,
    'Recuperados':11692,
    'Fallecidos':3150
    })
SON={}
SON['Casos']=[]
SON['Casos'].append({
    'Confirmados':24418,
    'Negativos':20782,
    'Sospechosos':1779,
    'Activos':501,
    'Recuperados':18017,
    'Fallecidos':2853
    })
TA={}
TA['Casos']=[]
TA['Casos'].append({
    'Confirmados':31691,
    'Negativos':33906,
    'Sospechosos':676,
    'Activos':736,
    'Recuperados':25740,
    'Fallecidos':2755
    })
def Estado():
    if combo.get()=='Aguascalientes':
        print("Estos son los casos en Aguascalietes:")
        print(ags['Casos'])
        print(" ")
    elif combo.get()=='Baja California Norte':
        print("Estos son los casos en Baja California Norte:")
        print(BC['Casos'])
        print(" ")
    elif combo.get()=='Baja California Sur':
        print("Estos son los casos en Baja California Sur:")
        print(BCS['Casos'])
        print(" ")
    elif combo.get()=='Campeche':
        print("Estos son los casos en Campeche:")
        print(Camp['Casos'])
        print(" ")
    elif combo.get()=='Chiapas':
        print("Estos son los casos en Chiapas:")
        print(Chis['Casos'])
        print(" ")
    elif combo.get()=='Queretaro':
        print("Estos son los casos en Queretaro:")
        print(QR['Casos'])
        print(" ")
    elif combo.get()=='San Luis Potosi':
        print("Estos son los casos en San Luis Potosi:")
        print(SLP['Casos'])
    elif combo.get()=='Sinaloa':
        print("Estos son los casos en Sinaloa:")
        print(SIN['Casos'])
        print(" ")
    elif combo.get()=='Sonora':
        print("Estos son los casos en Sonora:")
        print(SON['Casos'])
        print(" ")
    elif combo.get()=='Tabasco':
        print("Estos son los casos en Tabasco:")
        print(TA['Casos'])
        print(" ")
def guardar():
    if combo.get()=='Aguascalientes':
        with open('agscovid.json','w') as file:
            json.dump(ags,file)
    elif combo.get()=='Baja California Norte':
        with open('BCcovid.json','w') as file:
            json.dump(BC,file)
    elif combo.get()=='Baja California Sur':
        with open('BCScovid.json','w') as file:
            json.dump(BCS,file)
    elif combo.get()=='Campeche':
        with open('Campcovid.json','w') as file:
            json.dump(Camp,file)
    else:
        with open('Chiscovid.json','w') as file:
            json.dump(Chis,file)
    print("Los datos  han sido guardados correctamente")
    print(" ")
    
windows=Tk()
windows.title('Menu de Estados')
windows.geometry('720x404')

foto=PhotoImage(file='SemaforoCovid.png')
fondo=Label(windows,image=foto)
fondo.place(x=0,y=0)

texto=StringVar()
texto.set("Estado: ")

combo=Combobox(windows)
combo.place(x=300,y=175)
combo['value']=('Aguascalientes','Baja California Norte','Baja California Sur','Campeche','Chiapas',
                'Queretaro','San Lus Potosi','Sinaloa','Sonora','Tabasco')
combo.current()

boton=Button(windows,command=guardar,text="Guardar Datos")
btn=Button(windows,command=Estado,text="Entrar")
eti=Label(windows,textvariable=texto)
eti.place(x=250,y=175)

boton.place(x=400,y=300)
btn.place(x=250,y=300)

windows.mainloop()
input(" ")


