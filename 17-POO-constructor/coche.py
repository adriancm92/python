#Definición clase Coche
class Coche:
    
    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #color = 'Azul'
    #marca = 'Mazda'
    #modelo = 'MX-5'
    #velocidad = 280
    #caballaje = 140
    #cilindrada = 1.8
    #plazas = 2
    
    atributo_publico = "Soy un atributo público"
    __atributo_privado = "Soy un atributo privado"
    
    def __init__ (self, marca, modelo, año, cilindrada, caballos, color, velocidad, plazas):
        self.marca      = marca
        self.modelo     = modelo
        self.año        = año
        self.cilindrada = cilindrada
        self.caballos   = caballos
        self.color      = color
        self.velocidad  = velocidad
        self.plazas     = plazas
    
    #Métodos, son acciones que hace el objeto (coche) (funciones)
    def setMarca(self, marca):
        self.marca = marca
        
    def getMarca(self):
        return self.marca
    
    def setModelo(self, modelo):
        self.modelo = modelo
        
    def getModelo(self):
        return self.modelo
    
    def setAño(self, año):
        self.año = año
        
    def getAño(self):
        return self.año
    
    def setCilindrada(self, cilindrada):
        self.cilindrada = cilindrada
        
    def getCilindrada(self):
        return self.cilindrada
    
    def setCaballos(self, caballos):
        self.caballos = caballos
    
    def getCaballos(self):
        return self.caballos
    
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color    
    
    def accelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.frenar -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        info = "----- Información del coche -----"
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Año: " + str(self.getAño())
        info += "\n Cilindrada: " + str(self.getCilindrada())
        info += "\n Caballos: " + str(self.getCaballos())
        info += "\n Color: " + self.getColor()
        
        return info
    
    def getPrivado(self):
        return self.__atributo_privado
    
#Fin defición clase coche