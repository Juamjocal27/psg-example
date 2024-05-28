"""
Eres NOE y tiene que guardar dos animales de cada especie en un arca, 
crea un diccionario con las especies
"""
arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}
print(arca)
# Añade el arca 2 especies más usando update()
arca.update({"oveja": 2, "pavo": 2})
print(arca)

# Toma lista de los animales en el area iterando el diccionario
print(arca)
iterar = iter(arca.items())
print(iterar)
lista = next(iterar)
print(lista)
lista = next(iterar)
print(lista)
lista = next(iterar)
print(lista)
lista = next(iterar)
print(lista)
lista = next(iterar)
print(lista)
lista = next(iterar)
print(lista)
lista = next(iterar)
print(lista)
lista = next(iterar)
print(lista)

# Existe en el arca la especie 'dragón'?
existe = 'dragón' in arca
print("Existe en el arca la especie dragón: ", existe)

# Elimina la especie 'unicornio' del arca
print(arca)
arca.pop('unicornio')
print(arca)

# Modifica el valor de la especie 'jirafa' por 2
arca['jirafa'] = 2
print(arca)
# Vacia el arca después del diluvio
arca.clear()
print(arca)