"""
Modulos: son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, que los puedes consultar aquí:


Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos
"""

# Importar modulo
#import mimodulo
#from mimodulo import holaMundo
from time import process_time_ns
from mimodulo import *

#print(mimodulo.holaMundo("Adrián Cañuelo Martínez"))
#print(mimodulo.calculadora(3, 5, True))

print(holaMundo("Adrián Cañuelo Martínez"))
print(calculadora(3, 5, True))

#Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().time())

#Mdoculo matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Número Pi: ", float(math.pi))
print("Número Pi: ", math.pi)