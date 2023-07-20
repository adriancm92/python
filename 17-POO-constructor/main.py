from coche import Coche

vehiculo  = Coche("Ford", "Focus", 2019, 1.0, 120, "Gris", 240, 5)
vehiculo2 = Coche("Mazda", "MX-5", 1999, 1.8, 140, "Azul", 240, 2)
vehiculo3 = Coche("Hyundai", "i30", 2021, 1.0, 110, "Rojo", 240, 5)
vehiculo4 = Coche("Toyota", "Aygo", 2018, 1.0, 75, "Gris", 180, 4)

#print(carro.getMarca(), carro.getModelo(), carro.getColor())
print(vehiculo.getInfo())
print(vehiculo2.getInfo())
print(vehiculo3.getInfo())
print(vehiculo4.getInfo())

#Detectar tipado
#vehiculo2 = "Aleatorio"
if type(vehiculo2) == Coche:
    print("Es un objeto correcto!")
else:
    print("No es un objeto!")
    
#Visibilidad
print(vehiculo.atributo_publico)
#print(vehiculo.__atributo_privado)
print(vehiculo.getPrivado())
