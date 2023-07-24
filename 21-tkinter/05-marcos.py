from tkinter import *

ventana = Tk()
ventana.title("Adrián | Master en Python")
ventana.geometry("400x400")

marco_padre = Frame(ventana, width=150, height=150)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=150, height=150)
marco.config(
    bg="red",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial",12)
)

texto.pack(anchor=CENTER, fill=Y, expand=YES)

marco = Frame(marco_padre, width=150, height=150)
marco.config(
    bg="green",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=150, height=150)
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco = Frame(marco_padre, width=150, height=150)
marco.config(
    bg="blue",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=150, height=150)
marco.config(
    bg="orange",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT)

ventana.mainloop()