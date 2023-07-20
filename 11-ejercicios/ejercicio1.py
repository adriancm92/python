"""
Ejercicio 1. Hacer un programa que tenga una lista 
    de 8 números enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer la funcion que recorra la lista de números y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algún elemento (que el usuario pida por teclado)
"""

numeros = [3,6,96,54,32,7,21,64]

#Recorrer y mostrar la lista
print("####### Recorrer y mostrar la lista #######")
for numero in numeros:
    print(numero)

#Función que recorre la lista y devuelve un string
def mostrarLista(lista):
    resultado = "####### Listado Función #######"
    resultado += "\n"
    
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
        
    return resultado
    
print(mostrarLista(numeros))

#Ordenar y mostrar la lista
print("####### Ordenar y mostrar la lista #######")
numeros.sort()
print(mostrarLista(numeros))

#Mostrar la longitud de la lista
print("####### Longitud de la lista #######")
print(len(numeros))

#Buscar en la lista
print("####### Búsqueda en la lista #######")
busqueda = int(input("Introduce un número a buscar: "))

comprobacion = isinstance(busqueda, int)

while not comprobacion or busqueda <= 0:
    print("Debes de introducir un numero y que sea maor a 0.")
    busqueda = int(input("Introduce un número a buscar: "))
else:
    print(f"Has introducido el: {busqueda}")
    
print(f"####### Buscar en la lista el número {busqueda} #######")

search = numeros.index(busqueda)
print(f"El número buscado existe en la lista, es el indice: {search}")
