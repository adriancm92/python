#Importar modulo
import sqlite3

#Conexión
conexion = sqlite3.connect('pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
"""
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255)"+
")")
"""

#Guardar cambios
#conexion.commit()

#Insertar datos
#cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de mi producto', 550)")
#conexion.commit()

#Borrar registros
#cursor.execute("DELETE FROM productos")
#conexion.commit()

#Insertar varios registros
"""
productos = [
    ("Ordenador portatil", "Notebook Asus", 1299),
    ("Ordenador sobremesa", "PC Razer", 999),
    ("Placa Base", "Asus B760 ATX", 299),
    ("Tarjeta Grafica", "Asus RTX 4070", 659),
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()
"""

#Actualizar registro
cursor.execute("UPDATE productos SET precio=570 WHERE id=11")
conexion.commit()

#Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 0;")
productos = cursor.fetchall()

for producto in productos:
    print("ID producto:", producto[0])
    print("Nombre:", producto[1])
    print("Descripción:", producto[2])
    print("Precio:", producto[3])
    print("\n")

#cursor.execute("SELECT titulo FROM productos;")
#producto = cursor.fetchone()
#print(producto)

#Cerrar conexión
conexion.close()