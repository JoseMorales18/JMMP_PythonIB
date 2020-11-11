import mysql.connector
from tkinter import *
from tkinter.ttk import *
        
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="",
database="covid mx")


def agregar():
    mycursor=mydb.cursor()
    sql="INSERT INTO estados (control,estado) VALUES (%s,%s)"
    c1=input("control de estado: ")
    est=input("estado: ")
    val=(c1,est)
    mycursor.execute(sql,val)

    mydb.commit()
    agregar2()
def agregar2():
    mycursor=mydb.cursor()
    sql="INSERT INTO datos (control,confirmados,recuperados,\
    defunciones,activos) VALUES (%s,%s,%s,%s,%s)"
    a=input("control: ")
    b=input("confirmados: ")
    c=input("recuperados: ")
    d=input("defunciones: ")
    e=input("activos: ")
    val=(a,b,c,d,e)
    mycursor.execute(sql,val)

    mydb.commit()
    print(mycursor.rowcount,"estado agregado")
    
def Estado():
    print('Confirmados','Recuperados','Defunciones','Activos')
    if combo.get()=='Chihuahua':
        mycursor=mydb.cursor()

        sql="SELECT \
            datos.Confirmados AS ala, \
            datos.Recuperados AS ale, \
            datos.Defunciones AS ali, \
            datos.Activos AS al0, \
            tipo.controld AS fav \
            FROM datos\
            INNER JOIN tipo ON datos.control=tipo.controld\
            where controld='1'"

        mycursor.execute(sql)
        myresult=mycursor.fetchall()

        for x in myresult:
            print (x)
    if combo.get()=='Coahuila':
        mycursor=mydb.cursor()

        sql="SELECT \
            datos.Confirmados AS ala, \
            datos.Recuperados AS ale, \
            datos.Defunciones AS ali, \
            datos.Activos AS al0, \
            tipo.controld AS fav \
            FROM datos\
            INNER JOIN tipo ON datos.control=tipo.controld\
            where controld='2'"

        mycursor.execute(sql)
        myresult=mycursor.fetchall()

        for x in myresult:
            print (x)
    if combo.get()=='Durango':
        mycursor=mydb.cursor()

        sql="SELECT \
            datos.Confirmados AS ala, \
            datos.Recuperados AS ale, \
            datos.Defunciones AS ali, \
            datos.Activos AS al0, \
            tipo.controld AS fav \
            FROM datos\
            INNER JOIN tipo ON datos.control=tipo.controld\
            where controld='3'"

        mycursor.execute(sql)
        myresult=mycursor.fetchall()

        for x in myresult:
            print (x)
    if combo.get()=='Nuevo Leon':
        mycursor=mydb.cursor()

        sql="SELECT \
            datos.Confirmados AS ala, \
            datos.Recuperados AS ale, \
            datos.Defunciones AS ali, \
            datos.Activos AS al0, \
            tipo.controld AS fav \
            FROM datos\
            INNER JOIN tipo ON datos.control=tipo.controld\
            where controld='4'"

        mycursor.execute(sql)
        myresult=mycursor.fetchall()

        for x in myresult:
            print (x)
    if combo.get()=='Zacatecas':
        mycursor=mydb.cursor()

        sql="SELECT \
            datos.Confirmados AS ala, \
            datos.Recuperados AS ale, \
            datos.Defunciones AS ali, \
            datos.Activos AS al0, \
            tipo.controld AS fav \
            FROM datos\
            INNER JOIN tipo ON datos.control=tipo.controld\
            where controld='5'"

        mycursor.execute(sql)
        myresult=mycursor.fetchall()

        for x in myresult:
            print (x)
    
        
        
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
combo['value']=('Chihuahua','Coahuila','Durango','Nuevo Leon','Zacatecas')
combo.current()

btn=Button(windows,command=Estado,text="Entrar")
bot=Button(windows,command=agregar,text="Agregar").place(x=340,y=300)
eti=Label(windows,textvariable=texto)
eti.place(x=250,y=175)

btn.place(x=250,y=300)

windows.mainloop()
input(" ")
