# Crear una lista con 10 nombres de personas
nombres = ["Juan", "Jose", "Carlos", "Victor", "Miguel", "Maria", "Ines", "Elena", "Karina", "Marina"]

# Obtener una sublista de 2 a 7
sub_lista = nombres[2:7]
print(sub_lista)

# buscar si existe el nombre "Jhon" en la lista original
buscar = "Jhon"
print(nombres.count(buscar) != 0)

# Ordenar la sublista alfabeticamente
nombres.sort()
print(nombres)

# Ordenar la lista original alfabeticamente de forma descendente
nombres.sort(reverse=True)
print(nombres)