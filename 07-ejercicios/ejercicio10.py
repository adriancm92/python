"""
Ejercicio 10. El programa tien que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuántos han suspendido.
"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuántos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al \"Alumno {contador}\" ?"))
    
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
        
    contador += 1
    
print(f"\nAlumnos aprobados: {aprobados}")
print(f"\nAlumnos suspensos: {suspendidos}")