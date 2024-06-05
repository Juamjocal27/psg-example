# Imprimir un tablero de ajedre de 8x8 con los caracteres '#' y '*'

# Dimensiones del tablero
filas = 8
columnas = 8

# Crear el tablero de ajedrez
for i in range(filas):
    for j in range(columnas):
        if (i + j) % 2 == 0:
            print('#', end='')
        else:
            print('*', end='')
    print()  # Nueva línea después de cada fila
