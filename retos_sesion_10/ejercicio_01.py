"""
Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez que 
salen van a comer a una plaza de comidas. Ambos quieren saber que tan 
compatibles son viendo cuantos platos de comida tienen en común. A 
continuación tienes los platos de comida que ambos han ido pidiendo a los 
largo de sus citas
"""
anita = {"Sushi", "Pizza", "Tacos", "Hamburguesa", "Pasta", "Alitas"}
pepito = {"Pizza", "Tacos", "Ensalada", "Pasta", "Helado", "Milanesa"}

comun = anita.intersection(pepito)
print(comun)

'''
Si la cantidad platos de comida que tienen en comunes mayor a 50% 
entonces ambos seguirán saliendo
'''
cantidad = len(comun)
total = len(anita)
print(total)
porcentaje = (cantidad / total) * 100
print(porcentaje >= 50)