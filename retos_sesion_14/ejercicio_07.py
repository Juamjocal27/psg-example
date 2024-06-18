# Simular un tres en raya con funciones donde reciba las jugadas y devuelva el ganador hasta que alguien ingrese salir
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def revisar_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return tablero[0][i]
        
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]
        
        return None
    
def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

def tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        movimiento = input(f"Jugador {jugador_actual}, ingrese su jugada (fila, columna) o 'salir' para terminar: ")

        if movimiento.lower() == "salir":
            print("Juego terminado.")
            break

        try:
            fila, columna = map(int, movimiento.split(","))
            if tablero[fila][columna] != " ":
                print("Movimiento invalido, la casilla ya esta ocupada. Intente de nuevo.")
                continue
        except (ValueError, IndexError):
            print("Movimiento invalido. asegurese de ingresar fila y columna en el rango 0-2. Intente de nuevo.")
            continue

        tablero[fila][columna] = jugador_actual

        ganador = revisar_ganador(tablero)
        if ganador:
            imprimir_tablero(tablero)
            print(f"Jugador {ganador} gana!")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("Empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

tres_en_raya()
