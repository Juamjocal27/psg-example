# Crear un ciclo infinito que reciba un número por teclado y verifique si es un número primo, termina la ejecución si se ingresa el número

while True:
    numero = int(input("Ingrese numero: "))

    if numero == 0:
        break
    
    primo = True
    
    if numero < 2:
        primo = False
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break

    if primo:
        print(f'{numero} es un número primo')

    else: 
        print(f'{numero} no es un número primo')
        
print('Se presiono cero fin del programa')
