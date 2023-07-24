import mysql.connector

#Conexión
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="master_python"
)

#Estado de la conexión
#print(database)

#Cursor
cursor = database.cursor(buffered=True)

#Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
    
#Crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")


#Mostrar tablas
"""
cursor.execute("SHOW TABLES")

for tables in cursor:
    print(tables)
    
#Insertar registros
#cursor.execute("INSERT INTO vehiculos VALUES(null,'Mazda','MX-5','9500') ")

coches = [
    ('Mazda','MX-5',9100),
    ('Ford','Focus',12500),
    ('Hyundai','i30',11500),
    ('Toyota','Aygo',4500),
    ('Hyundai','i30',9700)
]

cursor.executemany("INSERT INTO vehiculos VALUES (NULL, %s, %s, %s)", coches)

database.commit()
"""

#Listar registros
cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()

print("---TODOS LOS COCHES---")
for coche in result:
    print(coche[1], coche[2], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

#Eliminar registros
"""
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Hyundai'")
database.commit()

print(cursor.rowcount, "borrados")
"""

#Actualizar
cursor.execute("UPDATE vehiculos SET modelo='Supra' WHERE marca='Toyota'")
database.commit()

print(cursor.rowcount, "actualizado")