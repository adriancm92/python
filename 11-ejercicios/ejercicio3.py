"""
Ejercicio 3. Programa que compruebe si una variable está vacia
y si está vacia, rellenarla con texto en minusculas y mostrarlo
en mayusculas.
"""

texto = " "

if len(texto.strip()) <= 0:
    texto = "Esto es un texto en minusculas"
    print(texto.upper())
else:
    print(f"El texto contiene: {texto}")