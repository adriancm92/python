#Programación orientada a objetos (POO o OOP)

#Definir una clase (molde para crear más objetos de este tipo)
#(Coche) con caracteristicas similares

class Coche:
    
    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    color = 'Azul'
    marca = 'Mazda'
    modelo = 'MX-5'
    velocidad = 280
    caballaje = 140
    cilindrada = 1.8
    plazas = 2
    
    #Métodos, son acciones que hace el objeto (coche) (funciones)
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
        
    def getModelo(self):
        return self.modelo
    
    def accelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.frenar -= 1
    
    def getVelocidad(self):
        return self.velocidad

#Fin defición clase coche
    
#Crear objetos | Instanciar la clase
coche = Coche()

coche.setColor('Rojo')
print("Coche 1:")
print(coche.marca, coche.getModelo(), coche.color)
print("Velocidad del coche actual: ", coche.velocidad)
coche.accelerar()
coche.accelerar()
print("Velocidad del coche actual: ", coche.velocidad)

print('------------------------------')

#Crear más objetos
coche2 = Coche()

coche2.setColor("Gris")
coche2.setModelo("3")

print("Coche 2:")
print(coche2.marca, coche2.getModelo(), coche2.getColor())
print(type(coche2))