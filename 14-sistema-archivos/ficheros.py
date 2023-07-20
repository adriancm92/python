from io import open
import pathlib
import shutil
import os

#Abrir archivo
#archivo = open("fichero_texto.txt", "a+")

#Alternativa abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

#Escribir
#archivo.write("****** Texto insertado desde Python ******\n")

#Cerrar
archivo.close()

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

#Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    #lista_frase = frase.split()
    #print(lista_frase)
    print("- " +frase.center(100))
    
#Copiar
#ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_new.txt"
#shutil.copyfile(ruta_original, ruta_nueva)

#Mover
#ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
#shutil.move(ruta_original, ruta_nueva)

#Eliminar
#ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_new.txt"
#os.remove(ruta_nueva)

#Comprobar si existe
ruta_comprobar = os.path.abspath("./") + "/fichero_copiado_new.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
    
    
else:
    print("El archivo NO existe")