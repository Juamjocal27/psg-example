# Imprimir los 20 primeros números de la serie fibonacci

numero = int(input("Introduce numero: "))
a, b = 0, 1
serie_fib = []

for i in range(numero):
    serie_fib.append(a)
    c = a + b
    a = b
    b = c

print(serie_fib)