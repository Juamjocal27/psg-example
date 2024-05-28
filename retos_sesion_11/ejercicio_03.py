# Crea un diccionario con las siguientes tuplas de animales
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
animales = dict(tupla)
# Del diccionario obtén y elimina el valor de la clave 'aves
print(animales)
aves = animales.pop('aves')
print(animales)
# Modifica el valor de la clave 'gato' por '🐈'
animales['gato'] = '🐈'
print(animales)
# Cambia la clave perro por perros y su valor por ['🐶','🐕']
animales['perro'] = ['🐶','🐕']
print(animales)