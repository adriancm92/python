"""
Ejercicio 4.
Crear un script que tenga 4 variables, una lista, un string,
un entero y un booleano y que imprima un mensaje
según el tipo de dato de cada variable. Usar funciones.
"""

def traducirTipo(tipo):
    resultado = None
    if tipo == list:
        resultado = "LISTA"
    elif tipo == str:
        resultado = "CADENA DE TEXTO"
    elif tipo == int:
        resultado = "ENTERO"
    elif tipo == bool:
        resultado = "BOOLEANO" 
    return resultado


def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    mensaje = ""
    
    if test:
        mensaje = f"El tipo de dato es: {traducirTipo(tipo)}"
        #mensaje = f"El tipo de dato es: {type(dato)}"
    else:
        mensaje = "El tipo de dato NO es valido"
    return mensaje

lista = ["Hola", 14]
texto = "Esto es un texto"
entero = 5
booleano = True

print(comprobarTipado(lista, list))
print(comprobarTipado(texto, str))
print(comprobarTipado(entero, int))
print(comprobarTipado(booleano, bool))
