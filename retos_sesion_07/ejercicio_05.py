palabra = "Anita lava la tina"

palabra = palabra.lower()
palabra = palabra.split()
palabra = ''.join(palabra)
print(palabra == palabra[::-1])
# Convertimos toda la palabra en minusculas
#palabra = palabra.lower()
# print(palabra)
# Separamos la lista donde haya un espacio
# palabra = palabra.split()
# Unimos la cadena sin espacios
# ca = ''.join(cadena)
# print(palabra == cadena[::-1])
# cadena = ''.join(char for char in cadena if char.isalnum())
# print(cadena)
# print(palabra == cadena[::-1])