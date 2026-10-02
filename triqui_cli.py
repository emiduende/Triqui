"""Juego de Triqui en consola con entrada estricta de enteros."""


def mostrar_tablero(tablero):
    """Muestra el tablero en la consola."""
    print("\n")
    for i in range(0, 9, 3):
        print(f"  {tablero[i] if tablero[i] else i+1} | {tablero[i+1] if tablero[i+1] else i+2} | {tablero[i+2] if tablero[i+2] else i+3}")
        if i < 6:
            print("  ---------")
    print("\n")


def verificar_ganador(tablero):
    """Verifica si hay un ganador o empate."""
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]

    for combo in combinaciones_ganadoras:
        if tablero[combo[0]] and tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]]:
            return tablero[combo[0]]

    if all(tablero):
        return "Empate"

    return None


def obtener_movimiento(tablero, jugador):
    """Obtiene el movimiento válido del jugador."""
    while True:
        try:
            posicion = int(input(f"Jugador {jugador}: Selecciona una casilla (1-9): "))
            if posicion < 1 or posicion > 9:
                print("Error: Ingresa un número entre 1 y 9.")
                continue
            if tablero[posicion - 1]:
                print("Error: Esa casilla ya está ocupada.")
                continue
            return posicion - 1
        except ValueError:
            print("Error: Debes ingresar un número entero.")


def jugar():
    """Ejecuta una partida de Triqui."""
    tablero = [None] * 9
    jugador_actual = "X"

    print("=" * 30)
    print("     BIENVENIDO A TRIQUI")
    print("=" * 30)

    while True:
        mostrar_tablero(tablero)
        posicion = obtener_movimiento(tablero, jugador_actual)
        tablero[posicion] = jugador_actual

        resultado = verificar_ganador(tablero)
        if resultado:
            mostrar_tablero(tablero)
            if resultado == "Empate":
                print("¡Es un empate!")
            else:
                print(f"¡Jugador {resultado} gana!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"


if __name__ == "__main__":
    jugar()
