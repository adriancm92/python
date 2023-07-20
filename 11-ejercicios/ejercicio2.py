"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista.
Plus: Usar while y for
"""

coleccion_for = []
coleccion_while = []
x = 0

for contador in range(0, 120):
    coleccion_for.append({contador})
    print("********* BUCLE FOR *********")
    print(f"Mostrando el elemento: {coleccion_for[contador]}")
    
while x < 120:
    coleccion_while.append({x})
    print("*****************************")
    print("******** BUCLE WHILE ********")
    print(f"Mostrando el elemento: {coleccion_while[x]}")
    x += 1