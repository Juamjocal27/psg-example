# Crear un script que pida un número entero y verifique si es par o impar usando operador ternario

numero = int(input("Número entero:"))

# if numero % 2 == 0:
#     print("El numero es par")

# else:
#     print("El número es impar")

resultado = "Número par" if numero % 2 == 0 else "Número impar"
print(resultado)