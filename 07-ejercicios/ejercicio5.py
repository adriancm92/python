"""
Ejercicio 5. Hacer un programa que muestre todos los número entre
dos números que diga el usuario.
"""

numero1 = int(input("Escribe un primer número: "))
numero2 = int(input("Escribe un segundo número: "))

if numero1 < numero2:
    for contador in range(numero1,numero2 + 1):
        print(contador)
else:
    print("El número 1 debe ser menor al número 2.")
