"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION          AVENTURA                DEPORTES
GTA             Assassins               FIFA 23
COD             Red Dead Decepcion 2    NBA 23           
PUGB            CyberPunk 2077          F1 2023
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA","COD","PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["Assassins","Red Dead Decepcion 2","CyberPunk 2077"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 23","NBA 23","F1 2023"]
    }
]

for categoria in tabla:
    print(f"----------------- {categoria['categoria']} -----------------")
    for juegos in categoria['juegos']:
        print(juegos)