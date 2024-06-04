'''
Un usuario ingresa su nombre y gustos musicales por teclado separados 
por coma, verifica si el usuario ingresó un nombre válido usando truthiness, 
convertir los gustos musicales en una lista y verifica si tiene el gusto 
rock en su lista de gustos musicales
'''
Nombre = "Jhon Doe"
Gustos_musicales = ("rock", "pop", "jazz")

usuario = input('Introduce usuario y gustos musicales separado por comas: ')

lista = usuario.split(",")
# Verificar si se ingreso un nombre valido
verificar = lista[0].strip() if usuario else None

if verificar:
    print('Bienvenido: ', verificar) 
else: 
    print('Ingrese los datos correctamente')

# Buscar rock en la lista
musica = lista[1:] if len(lista) > 1 else []
buscar = 'rock' in musica

if buscar:
    print('Se encontro rock en los gustos de', lista[0])
else:
    print('No se encontro rock en los gustos de', lista[0])


