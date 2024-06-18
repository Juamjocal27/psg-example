# Crear una función anónima para obtener el área de un círculo con radio 5
from math import pi

area_circulo = lambda radio: pi * radio ** 2

radio = 5
print(f"El area del circulo es: {area_circulo(radio)}")

# Se que no avanzamos la linea 2 pero tenia conocimientos de como importar modulos