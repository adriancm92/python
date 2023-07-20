"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "Adrián",
    "apellidos": "Cañuelo Martínez",
    "edad": "30"
}

#print(persona["nombre"])

#Lista de diccionarios

contactos = [
    {
        "nombre": "Adrián",
        "email": "adrian@email.com" 
    },
    
    {
        "nombre": "Maite",
        "email": "maite@email.com" 
    },
    
    {
        "nombre": "Xavi",
        "email": "xavi@email.com" 
    },
    
    {
        "nombre": "Nico",
        "email": "nico@email.com" 
    },
]

##contactos[1]["nombre"] = "AdrianK"
#print(contactos[1]["nombre"])

print("\nListado de contactos: ")
print("--------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("--------------------------------------")