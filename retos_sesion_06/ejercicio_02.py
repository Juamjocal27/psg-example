print("Construir el operador XNOR en Python")

print(not(True != True))
print(not(True != False))
print(not(False != True))
print(not(False != False))

def xor(a, b):
    xor = a and not b or not a and b
    return xor
print(not(xor(True, True)))
print(not(xor(True, False)))
print(not(xor(False, True)))
print(not(xor(False, False)))

