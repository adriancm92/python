"""
# Condicional IF

SI se cumple esta condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejectuan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones

"""

# Ejemplo 1
print("############# EJEMPLO 1 #############")

# color = "verde"
color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Enhorabuena!!!")
    print("El color es ROJO")
else:
    print("Color incorrecto!!!")
    