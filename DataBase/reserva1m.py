# ==========================================================
# Generador de datos para la tabla RESERVA.
#
# Atributos:
# - id_reserva (PK, autogenerado por PostgreSQL)
# - dni_pasajero (FK -> PASAJERO)
# - estado
# - numero_asiento
# - fecha
# - clase
#
# El DNI debe existir previamente en la tabla PASAJERO.
#
# Cambiar TOTAL_RESERVAS para generar distintos tamaños:
# 1_000
# 10_000
# 100_000
# 1_000_000
#
# En este proyecto se generan 2 millones de reservas.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random
from datetime import datetime, timedelta

TOTAL_RESERVAS = 2_000_000

os.makedirs("Data", exist_ok=True)

estados = [
    "Pendiente",
    "Confirmada",
    "Cancelada"
]

clases = [
    "Economica",
    "Ejecutiva",
    "Primera"
]

fecha_inicio = datetime(2024, 1, 1)
fecha_fin = datetime(2026, 12, 31)

dias = (fecha_fin - fecha_inicio).days

with open("Data/reservas.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_RESERVAS):

        # Solo DNIs existentes en PASAJERO
        dni_pasajero = str(random.randint(70000000, 71999999))

        estado = random.choice(estados)

        fila = random.randint(1, 40)
        letra = random.choice(["A", "B", "C", "D", "E", "F"])
        numero_asiento = f"{fila}{letra}"

        fecha = (
            fecha_inicio +
            timedelta(days=random.randint(0, dias))
        ).strftime("%Y-%m-%d")

        clase = random.choice(clases)

        writer.writerow([
            dni_pasajero,
            estado,
            numero_asiento,
            fecha,
            clase
        ])

        if (i + 1) % 100000 == 0:
            print(f"Generadas: {i + 1:,} reservas")

print(f"\nSe generaron {TOTAL_RESERVAS:,} reservas correctamente.")