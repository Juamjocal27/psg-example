"""
Crear un programa para crear una canasta de frutas, solicitar
 frutas por teclado y almacenar en una lista, si se ingresa "salir"
 termina la ejecución. Solo se permiten las siguientes frutas
 caso contrario lanzar una excepcion personalizada
"""

class FrutaNoPermitidaError(Exception):
    def __init__(self, fruta):
        super().__init__(f"La fruta '{fruta}' no está permitida en la canasta.")

frutas_permitidas = {"🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"}

def mostrar_frutas_permitidas():
    print("Frutas permitidas:", ", ".join(frutas_permitidas))

def canasta_de_frutas():
    canasta = []
    mostrar_frutas_permitidas()
    while True:
        fruta = input("Ingrese una fruta (o 'salir' para terminar): ")
        if fruta.lower() == "salir":
            print("Saliendo del programa.")
            break

        try:
            if fruta not in frutas_permitidas:
                raise FrutaNoPermitidaError(fruta)
            canasta.append(fruta)
            print(f"Fruta '{fruta}' agregada a la canasta.")
        except FrutaNoPermitidaError as e:
            print(e)
            mostrar_frutas_permitidas()

    print("Canasta de frutas:", canasta)

if __name__ == "__main__":
    canasta_de_frutas()