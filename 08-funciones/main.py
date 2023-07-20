
def primeraFuncion(nombre):
    print(f"Tu nombre es: {nombre}")

#Ejemplo 1
print("######### EJEMPLO 1 #########")

#Realizamos la primera funcion sin parametros

nombre = input("¿Cual es tu nombre? ")

primeraFuncion(nombre)

#Ejemplo 8
print("######### EJEMPLO 8 #########")

funcion_anyo = lambda year: f"El año es: {year}"

year = input("Escribe un año: ")

print(funcion_anyo(year))