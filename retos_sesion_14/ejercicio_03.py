# Crear una función recursiva para obtener el N número de la serie de Fibonacci
def serie_fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return serie_fibonacci(num-1) + serie_fibonacci(num-2)

num = 9
print(f"El {num}-ésimo número de la serie de Fibonacci es: {serie_fibonacci(num)}")
