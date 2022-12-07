import pymysql
import tkinter
from tkinter import *
conexion = pymysql.connect(user='ceva', password='Juliodelgado1451',
                                    host='localhost',
                                    db='horario'
                                    )
print(conexion)
cursor = conexion.cursor()
""" x = 23
sql = f"INSERT INTO hora(hora,minuto) VALUES('{x}','23')"
cursor.execute(sql)
 """
base = []
sql1 = "SELECT * FROM hora"
cursor.execute(sql1)
tablas = cursor.fetchall()
for tabla in tablas:
    print(tabla)
    base.append(tabla)
conexion.commit()
print(base)
def mostrar():
    for i in base:
        label1 = Label(ventana,text=i)
        label1.pack(anchor=CENTER)
def enviar():
    mostrar = mensaje.get("1.0","end-1c")
    print(mostrar)
    print(len(mostrar))
ventana = tkinter.Tk()
ventana.title("App")
ventana.geometry("400x300")
boton = tkinter.Button(ventana, text="base de datos",command=mostrar)
boton.pack()
mensaje = Text(ventana,width=30,height=10)
mensaje.pack()
botona = Button(ventana,text="Enviar datos",command=enviar)
botona.pack()
label = Label(ventana, text="id,numero,numero")
label.pack(anchor=CENTER)
ventana.mainloop()
