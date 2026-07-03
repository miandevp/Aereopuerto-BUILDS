# ==========================================================
# Generador de datos para la tabla AREA.
#
# Atributos:
# - id_area (PK)
# - capacidad
#
# Cambiar TOTAL_AREAS para generar distintos tamaños:
# 100
# 500
# 1_000
# 5_000
#
# En este proyecto se generan 1,000 áreas.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random

TOTAL_AREAS = 1_000

os.makedirs("Data", exist_ok=True)

with open("Data/areas.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_AREAS):

        id_area = i + 1
        capacidad = random.randint(10, 300)

        writer.writerow([
            id_area,
            capacidad
        ])

        if (i + 1) % 100 == 0:
            print(f"Generadas: {i + 1:,} áreas")

print(f"\nSe generaron {TOTAL_AREAS:,} áreas correctamente.")