"""
Calculadora flexible: Crea una calculadora que acepte diferentes operaciones
matemáticas como argumentos de palabras clave y realice los cálculos
correspondientes, las operaciones son suma, resta, multiplicación y división
"""
def calculadora(**operacion):
    resultado = None
    if "suma" in operacion:
        resultado = sum(operacion['suma'])
    elif "resta" in operacion:
        resultado = operacion["resta"][0]
        for num in operacion["resta"][1:]:
            resultado -= num
    elif "multiplicacion" in operacion:
        resultado = 1
        for num in operacion["multiplicacion"]:
            resultado *= num
    elif "division" in operacion:
        resultado = operacion["division"][0]
        for num in operacion["division"][1:]:
            resultado /= num
    return resultado

print(calculadora(suma=[1, 2]))
print(calculadora(resta=[16, 10]))
print(calculadora(multiplicacion=[8, 2]))
print(calculadora(division=[12, 3]))