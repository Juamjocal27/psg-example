palabra = "Anita lava la tina"

#cadena = palabra.lower()
#cadena = ''.join(char for char in cadena if char.isalnum())
cadena = palabra.strip(" ")
print(cadena)
print(cadena == cadena[::-1])