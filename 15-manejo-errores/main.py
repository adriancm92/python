#Capturar excepciones y manejar errores en código
#susceptible a fallos/errores
"""
try:
    nombre = input("Indica tu nombre para el registro: ")
    
    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre
        
    print(nombre_usuario)
    
except:
    print("Ha ocurrido un error, no se puede dejar el nombre vacío")
else:
    print("Se ha registrado correctamente el nombre!")
finally:
    print("Ha finalizado el registro!")
"""

#Multiples excepciones
"""
try:
    numero = int(input("Número para elevarlo al cuadrado: "))
    print("El cuadrado es: " +str(numero*numero))    
except TypeError:
    print("Ha ocurrido un error, no se puede dejar el nombre vacío")
#except ValueError:
#    print("Introduce un número correcto!")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)
"""
#Excepciones personalizadas o lanzar excepciones
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 1 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido al Master en Python, {nombre}")
except ValueError:
    print("Introduce los datos correctamente!")
except Exception as e:
    print("Ha ocurrido un error:", type(e).__name__)