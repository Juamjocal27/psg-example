# Crea un diccionario para almacenar información de comidas de animales por ejemplo
comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}

# Añade al diccionario de comidas 4 alimentos más usando update(clave=valor)
comidas.update({"Forraje": ["Vaca", "Oveja"], "Ensilaje": ["Vaca", "Cabra" ], "Cereales": ["Conejos", "Cuyes"], "Grano": ["Pollos", "Pavos"]})
print(comidas)
# Existe en el diccionario de comidas la comida 'carne'?
Existe = 'carne' in comidas
print("Carne en comidas", Existe)
# Elimina la comida 'frutas' del diccionario de comidas
eliminar = comidas.pop('frutas')
print("Se elimino animales que comen fruta: ", eliminar)
print(comidas)