# ==========================================================
# Generador de datos para la tabla RESERVA.
#
# Atributos:
# - id_reserva (PK)
# - dni_pasajero (FK -> PASAJERO)
# - fecha
# - estado
# - numero
# - clase
#
# El archivo CSV se genera SIN CABECERA.
# ==========================================================

import csv
import os
import random
from datetime import datetime, timedelta

TOTAL_RESERVAS = 1_000

os.makedirs("Data1k", exist_ok=True)

# Leer todos los pasajeros existentes
pasajeros = []

with open("Data1k/pasajeros.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        pasajeros.append(fila[0])

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

with open("Data1k/reservas.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_RESERVAS):

        id_reserva = i + 1

        # FK válida hacia PASAJERO
        dni_pasajero = random.choice(pasajeros)

        fecha = (
            fecha_inicio +
            timedelta(days=random.randint(0, dias))
        ).strftime("%Y-%m-%d")

        estado = random.choice(estados)

        fila = random.randint(1, 40)
        letra = random.choice(["A", "B", "C", "D", "E", "F"])
        numero = f"{fila}{letra}"

        clase = random.choice(clases)

        writer.writerow([
            id_reserva,
            dni_pasajero,
            fecha,
            estado,
            numero,
            clase
        ])

        if (i + 1) % 100000 == 0:
            print(f"Generadas: {i + 1:,} reservas")

print(f"\nSe generaron {TOTAL_RESERVAS:,} reservas correctamente.")