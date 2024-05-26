"""
Dos mochileros se encuentran en el Salar de Uyuni y se ponen a comparar 
la cantidad de lugares que han visitado

Cada uno quiere saber en que parte del mundo ha estado el otro que el no 
haya visitado
"""

mochilero_a = {"París", "Londres", "Nueva York", "Tokio", "Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney", "Argentina","Brasil","Panama","Bolivia"}

no_visitado_a = mochilero_b.difference(mochilero_a)
no_visitado_b = mochilero_a.difference(mochilero_b)

print("mochilero a no visito", no_visitado_a)
print("mochilero b no visito", no_visitado_b)

# Ahora quieren saber en que ciudades han estado ambos mochileros

comun = mochilero_a.intersection(mochilero_b)
print("Lugares en común: ", comun)