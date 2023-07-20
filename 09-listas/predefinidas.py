amigos = ['Iván', 'Pedro', 'Alejandro', 'Pablo', 'Xavi', 'Nico']
numeros = [1, 2, 5, 8, 3, 4]

print(amigos)

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos
amigos.append("Victor")
amigos.insert(1,"Fran")

print(amigos)

#Eliminar elementos
amigos.pop(4)
amigos.remove("Alejandro")

print(amigos)

#Dar la vuelta
amigos.reverse()
print(amigos)

#Buscar dentro de una lista
print("Pedro" in amigos)

#Contar elementos
print(len(amigos))

#Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

#Conseguir indice
print(amigos.index("Victor"))

#Unir listas
amigos.extend(numeros)
print(amigos)