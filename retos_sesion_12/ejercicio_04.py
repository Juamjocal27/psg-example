'''
Una tienda ofrece descuentos a sus clientes, si el cliente es mayor de edad 
y tiene una compra mayor a 1000, se le aplica un descuento del 10%, si es 
menor de edad y tiene una compra mayor a 500 se le aplica un descuento 
del 5%, si no cumple ninguna condición se le aplica un descuento del 2%
'''
def pagar(Descuento):
     pague = compra - ((compra * Descuento) / 100)
     return pague

edad = int(input('Edad: '))
compra = int(input('Compra: '))

if edad >= 18 and compra >= 1000:
    descuento = compra - ((compra * 10) / 100)
    print('Descuento de 10% pague: ', pagar(10))
elif edad < 18 and compra >= 500:
    print('Descuento de 5% pague: ', pagar(5))
else:
    print('Descuento de 2% pague: ', pagar(2))