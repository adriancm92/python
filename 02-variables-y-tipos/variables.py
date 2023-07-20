"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto.
"""


#Crear variables y asignar
texto = "Máster en Python"
texto2 = "Adrián CM"
numero = 28
decimal = 8.8

#Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("--------------------------------------------")

#Sustituir el valor de algunas variables / reasignando valores
numero = 25
decimal = 2.5

print(numero)
print(decimal)

print("--------------------------------------------")

#Concetancion
nombre = "Adrian"
apellidos = "CM"
edad = "28/0/1992"

print(nombre + " " + apellidos + " " + edad)
print(f"{nombre} {apellidos} - {edad}")
print("Hola me llamo {} {} y mi edad es: {}".format(nombre, apellidos, edad))

print(nombre, apellidos, edad)