# Imprimir los 20 primeros número primos

primos = []
numero = 2  # El primer número a verificar

while len(primos) < 20:
    es_primo = True

    if numero < 2:
        es_primo = False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(numero)

    numero += 1

print(primos)