from tkinter import *

ventana = Tk()
ventana.geometry("500x400")
ventana.title("Formularios en Tkinter | Adrián CM")

#Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Adrián CM")
encabezado.config(
    fg="white",
    bg="darkgrey",
    font=("Open Sans",18),
    padx=10,
    pady=10
)
encabezado.pack(side=LEFT, anchor=NW)

ventana.mainloop()