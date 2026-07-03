# ==========================================================
# Generador de datos para la tabla PUERTA_EMBARQUE.
#
# Atributos:
# - numero_puerta (PK)
# - id_area (FK -> AREA_EMBARQUE)
# - estado
#
# El id_area debe existir previamente en la tabla
# AREA_EMBARQUE.
#
# Cambiar TOTAL_PUERTAS para generar distintos tamaños:
# 100
# 500
# 1_000
#
# En este proyecto se generan 1,000 puertas.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random

TOTAL_PUERTAS = 1_000

os.makedirs("Data", exist_ok=True)

# Leer únicamente las áreas de embarque
areas_embarque = []

with open("Data/area_embarque.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        areas_embarque.append(int(fila[0]))

estados = [
    "Disponible",
    "Ocupada",
    "Mantenimiento"
]

with open("Data/puertas_embarque.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_PUERTAS):

        numero_puerta = i + 1
        id_area = random.choice(areas_embarque)
        estado = random.choice(estados)

        writer.writerow([
            numero_puerta,
            id_area,
            estado
        ])

        if (i + 1) % 100 == 0:
            print(f"Generadas: {i + 1:,} puertas")

print(f"\nSe generaron {TOTAL_PUERTAS:,} puertas de embarque correctamente.")