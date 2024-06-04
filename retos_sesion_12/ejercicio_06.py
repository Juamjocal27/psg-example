'''
Crea una calculadora por consola que realice las operaciones de suma, 
resta, multiplicación y división, ingresa dos números y la operación a 
realizar, verifica si la operación es válida y muestra el resultado
'''

# Número 1: 10
# Número 2: 5
# Operación: +
# -------------
# Resultado: 15

numero_1 = float(input('Ingrese numero 1: '))
numero_2 = float(input('Ingrese numero 2: '))
operacion = input('Operacion (+, -, *, /):')

if operacion == '+':
    print('suma', numero_1 + numero_2)
elif operacion == '-':
    print('resta', numero_1 - numero_2)
elif operacion == '*':
    print('multiplicacion', numero_1 * numero_2)
elif operacion == '/' and numero_2:
    print('division', numero_1 / numero_2)
else:
    print('Operación no valida')
