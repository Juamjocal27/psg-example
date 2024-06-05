# Crea un ciclo infinito que reciba una palabra por teclado y verifique si es palindrome, termina la ejecución si se ingresa la palabra 'salir'

while True:
    palabra = input("Ingresa una palabra (o 'salir' para terminar): ")
    
    if palabra.lower() == 'salir':
        break
    
    # Verificar si la palabra es un palíndromo
    if palabra == palabra[::-1]:
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' no es un palíndromo.")

print("Programa terminado.")