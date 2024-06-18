# Crear una funcion que reciba una lista de números y devuelva solo los numeros pares

def filtrar_numeros_pares(lista_numeros):
    numeros_pares = [numero for numero in lista_numeros if numero % 2 == 0]
    return numeros_pares

lista = range(1,10)
resultado = filtrar_numeros_pares(lista)
print(resultado)