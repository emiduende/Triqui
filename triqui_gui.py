"""Juego de Triqui con interfaz gráfica usando CustomTkinter."""

import customtkinter as ctk
from tkinter import messagebox


class TriquiGUI:
    """Clase principal del juego Triqui con interfaz gráfica."""

    def __init__(self, root):
        self.root = root
        self.root.title("Triqui - Tic-Tac-Toe")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.tablero = [None] * 9
        self.jugador_actual = "X"
        self.juego_activo = True
        self.victorias_x = 0
        self.victorias_o = 0
        self.botones = []

        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea la interfaz gráfica principal."""
        # Panel superior con información
        panel_superior = ctk.CTkFrame(self.root, fg_color="#1E1E2E")
        panel_superior.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(panel_superior, text="TRIQUI", font=("Arial", 24, "bold"), text_color="#89B4FA").pack()

        self.etiqueta_turno = ctk.CTkLabel(panel_superior, text=f"Turno: {self.jugador_actual}",
                                           font=("Arial", 14), text_color="#89B4FA")
        self.etiqueta_turno.pack()

        # Marco del tablero
        frame_tablero = ctk.CTkFrame(self.root, fg_color="#1E1E2E")
        frame_tablero.pack(pady=10, padx=10)

        for i in range(9):
            fila = i // 3
            columna = i % 3
            boton = ctk.CTkButton(frame_tablero, text="", width=80, height=80,
                                 font=("Arial", 32, "bold"),
                                 fg_color="#313244", text_color="#CDD6F4",
                                 hover_color="#45475A",
                                 command=lambda idx=i: self.realizar_movimiento(idx))
            boton.grid(row=fila, column=columna, padx=5, pady=5)
            self.botones.append(boton)

        # Panel de marcador
        panel_marcador = ctk.CTkFrame(self.root, fg_color="#1E1E2E")
        panel_marcador.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(panel_marcador, text=f"X: {self.victorias_x}",
                     font=("Arial", 12), text_color="#A6E3A1").pack(side="left", padx=20)
        ctk.CTkLabel(panel_marcador, text=f"O: {self.victorias_o}",
                     font=("Arial", 12), text_color="#F38BA8").pack(side="right", padx=20)

        # Botón para reiniciar
        ctk.CTkButton(self.root, text="Reiniciar Juego", command=self.reiniciar,
                      fg_color="#89B4FA", text_color="#1E1E2E",
                      font=("Arial", 12, "bold")).pack(pady=10)

    def realizar_movimiento(self, indice):
        """Realiza un movimiento en la casilla especificada."""
        if not self.juego_activo or self.tablero[indice]:
            return

        self.tablero[indice] = self.jugador_actual
        self.botones[indice].configure(text=self.jugador_actual)

        if self.jugador_actual == "X":
            self.botones[indice].configure(text_color="#A6E3A1")
        else:
            self.botones[indice].configure(text_color="#F38BA8")

        ganador = self.verificar_ganador()
        if ganador:
            self.finalizar_juego(ganador)
            return

        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"
        self.etiqueta_turno.configure(text=f"Turno: {self.jugador_actual}")

    def verificar_ganador(self):
        """Verifica si hay un ganador."""
        combinaciones = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]

        for combo in combinaciones:
            if (self.tablero[combo[0]] and
                self.tablero[combo[0]] == self.tablero[combo[1]] == self.tablero[combo[2]]):
                self.resaltar_ganador(combo)
                return self.tablero[combo[0]]

        if all(self.tablero):
            return "Empate"

        return None

    def resaltar_ganador(self, combo):
        """Resalta las casillas ganadoras."""
        for indice in combo:
            self.botones[indice].configure(fg_color="#A6E3A1")

    def finalizar_juego(self, resultado):
        """Finaliza el juego y muestra el resultado."""
        self.juego_activo = False

        for boton in self.botones:
            boton.configure(state="disabled")

        if resultado == "Empate":
            messagebox.showinfo("Resultado", "¡Es un empate!")
        else:
            if resultado == "X":
                self.victorias_x += 1
            else:
                self.victorias_o += 1
            messagebox.showinfo("Resultado", f"¡Jugador {resultado} gana!")

        self.reiniciar()

    def reiniciar(self):
        """Reinicia el juego."""
        self.tablero = [None] * 9
        self.jugador_actual = "X"
        self.juego_activo = True
        self.etiqueta_turno.configure(text=f"Turno: {self.jugador_actual}")

        for i, boton in enumerate(self.botones):
            boton.configure(text="", fg_color="#313244", state="normal", text_color="#CDD6F4")


def main():
    root = ctk.CTk()
    app = TriquiGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
