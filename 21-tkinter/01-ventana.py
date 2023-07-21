#Tkinter
#Módulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path


class Programa:
    
    def __init__(self):
        self.title = "Interfaz gráfica con Python"
        self.icon = os.path.abspath("./imagenes/logotipo.ico")
        self.icon_alt = os.path.abspath("./21-tkinter/imagenes/icono.ico")
        self.size = "750x450"
        self.resizable = False

    def cargar(self):
        #Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana
        
        #Titulo de la ventana
        ventana.title(self.title)

        #Comprobar si existe un archivo
        ruta_icono = self.icon

        if not os.path.isfile(ruta_icono):
            ruta_icono = self.icon_alt

        #Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        #Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        #Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        #Bloquear/Permitir el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
        
    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()
        
    def mostrar(self):
        #Arrancar y mostrar la ventana hasta que la cierres
        self.ventana.mainloop()
    
    
#Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("Este es un nuevo texto desde el método")
programa.addTexto("Probando segundo texto")
programa.addTexto("Para el curso Python")
programa.addTexto("Último texto")
programa.mostrar()
