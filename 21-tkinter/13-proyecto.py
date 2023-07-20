"""
Crear un programa que tenga:
- Ventana --> OK
- Tamaño Fijo --> OK
- No redimensionable --> OK
- Un menu (Inicio, Añadir, Información y Salir) --> OK
- Opción de salir de la aplicacion --> OK
- Diferentes pantallas --> OK
- Formulario de añadir productos
- Guardar datos temporalemnte
- Mostrar todos los datos listados en una pantalla home

"""

from ctypes import alignment
from tkinter import *
from tkinter.tix import COLUMN

#Creamos la ventana, tamaño y no redimensionable
ventana = Tk()
ventana.geometry("300x300")
ventana.title("Proyecto Tkinter - Adrian CM")
ventana.resizable(0,0)


#Pantallas
def inicio():
    inicio_label.config(
        fg="white",
        bg="black",
        font=("Arial",18),
        padx=122,
        pady=20
    )
    inicio_label.grid(row=0, column=0)

    #Ocultar resto de pantallas
    anyadir_label.grid_remove()
    anyadir_name_label.grid_remove()
    anyadir_name_entry.grid_remove()

    info_label.grid_remove()
    by_label.grid_remove()
    

    return True

def anyadir():
    anyadir_label.config(
        fg="white",
        bg="black",
        font=("Arial",18),
        padx=62,
        pady=20
    )
    anyadir_label.grid(row=0, column=0, columnspan=10)

    #Campos del formulario
    anyadir_name_label.grid(row=1,column=0, padx= 5, pady=5, sticky=E)
    anyadir_name_entry.grid(row=1,column=1, padx= 5, pady=5, sticky=W)

    #Ocultar resto de pantallas
    inicio_label.grid_remove()
    info_label.grid_remove()
    by_label.grid_remove()

    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial",18),
        padx=87,
        pady=20
    )
    info_label.grid(row=0, column=0)    
    by_label.grid(row=1, column=0)

    #Ocultar resto de pantallas
    inicio_label.grid_remove()
    anyadir_label.grid_remove()

    return True

#Variables
name_data = StringVar()
price_data = StringVar()

#Definir campos de pantallas
inicio_label = Label(ventana, text="Inicio")
anyadir_label = Label(ventana, text="Añadir Producto")
info_label = Label(ventana, text="Información")
by_label = Label(ventana,text="Creado por Adrian CM - 2022")

#Campos del formulario
anyadir_name_label = Label(ventana, text="Nombre:")
anyadir_name_entry = Entry(ventana, textvariable=name_data)

#Cargar pantalla inicio
inicio()

#Creamos el menú
menu_principal = Menu(ventana)
menu_principal.add_command(label="Inicio", command=inicio)
menu_principal.add_command(label="Añadir", command=anyadir)
menu_principal.add_command(label="Información", command=info)
menu_principal.add_command(label="Salir", command=ventana.quit)
ventana.config(menu=menu_principal)

ventana.mainloop()