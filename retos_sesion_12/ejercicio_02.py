""" Tienes una página web y un usuario quiere acceder a ella, 
 verifica si el usuario inicio sesión para acceder a la pagina, 
caso contrario muestra un mensaje de error"""

opcion = input("Iniciar sesión (s/n)?: ").lower()

if opcion == 's':
    print('Ingrese usuario: ')

elif opcion == 'n':
    print('¡No inicio sesión!')
else: 
    print('¡Error al iniciar sesión!')
