# Desarrollo del Juego Triqui (Tic-Tac-Toe) en Python

Este repositorio contiene una implementación completa del clásico juego del **Triqui (Tres en Raya / Tic-Tac-Toe)** en Python, con dos versiones: una en consola y otra con interfaz gráfica moderna.

## 🎮 Versiones

### 1. **Versión Consola (CLI)**
- Interfaz interactiva basada en menús numéricos
- Entrada estricta de enteros (1-9)
- Control robusto de excepciones
- Ideal para ejecución en terminal

### 2. **Versión Gráfica (GUI)**
- Interfaz moderna con **CustomTkinter**
- Modo oscuro elegante (`#1E1E2E` fondo, `#89B4FA` acentos)
- Tablero interactivo con botones `3×3`
- Programación Orientada a Objetos (POO)
- Marcador de victorias
- Resaltado de combinaciones ganadoras

## 📁 Estructura del Proyecto

```
triqui-python/
├── venv/                   # Entorno virtual aislado
├── requirements.txt        # Dependencias del proyecto
├── triqui_cli.py          # Implementación en consola
├── triqui_gui.py          # Implementación gráfica (POO + CustomTkinter)
└── README.md              # Esta documentación
```

## 🛠️ Requisitos Previos e Instalación

### Crear y Activar el Entorno Virtual

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar Dependencias

```bash
pip install -r requirements.txt
```

## 🚀 Cómo Jugar

### Versión Consola
```bash
python triqui_cli.py
```
- Ingresa números del 1 al 9 para seleccionar casillas
- El juego verifica automáticamente validaciones

### Versión Gráfica
```bash
python triqui_gui.py
```
- Haz clic en cualquier casilla disponible
- El juego desabilita automáticamente casillas ocupadas
- Presiona "Reiniciar Juego" para una nueva partida

## 🎯 Reglas del Juego

1. **Turnos Alternados:** Jugador X y Jugador O se turnan
2. **Condición de Victoria:** 3 símbolos iguales en línea:
   - Horizontales: (1-2-3), (4-5-6), (7-8-9)
   - Verticales: (1-4-7), (2-5-8), (3-6-9)
   - Diagonales: (1-5-9), (3-5-7)
3. **Empate:** Si el tablero se llena sin ganador
4. **Finalización:** Una sola ronda por partida, luego reinicio automático

## 🎨 Paleta de Colores (GUI)

- **Fondo:** `#1E1E2E` (gris oscuro)
- **Acentos:** `#89B4FA` (azul)
- **Jugador X:** `#A6E3A1` (verde)
- **Jugador O:** `#F38BA8` (rojo/rosa)
- **Ganador:** `#A6E3A1` (verde brillante)

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

---

**Desarrollo:** Python 3.10+  
**Dependencias:** CustomTkinter >= 5.2.0
