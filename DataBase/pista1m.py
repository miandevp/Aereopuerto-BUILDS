# ==========================================================
# Generador de datos para la tabla PISTA.
#
# Atributos:
# - numero_pista (PK)
# - longitud
# - estado
#
# Cambiar TOTAL_PISTAS para generar distintos tamaños:
# 100
# 500
# 1_000
# 5_000
#
# En este proyecto se generan 1,000 pistas.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random

TOTAL_PISTAS = 1_000

os.makedirs("Data", exist_ok=True)

estados = [
    "Disponible",
    "Mantenimiento",
    "Cerrada"
]

with open("Data/pistas.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_PISTAS):

        numero_pista = i + 1

        # Longitud en metros (realista)
        longitud = random.randint(1800, 4500)

        estado = random.choice(estados)

        writer.writerow([
            numero_pista,
            longitud,
            estado
        ])

        if (i + 1) % 100 == 0:
            print(f"Generadas: {i + 1:,} pistas")

print(f"\nSe generaron {TOTAL_PISTAS:,} pistas correctamente.")