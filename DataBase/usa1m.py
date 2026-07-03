# ==========================================================
# Generador de datos para la tabla USA_PISTA.
#
# Atributos:
# - codigo_vuelo (FK -> VUELO)
# - numero_pista (FK -> PISTA)
#
# Relaciona los vuelos con las pistas utilizadas.
#
# Cambiar TOTAL_USOS para generar distintos tamaños:
# 1_000
# 10_000
# 100_000
# 1_000_000
# 2_000_000
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random

TOTAL_USOS = 1_000

os.makedirs("Data1k", exist_ok=True)

# Leer códigos de vuelo
vuelos = []

with open("Data1k/vuelos.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for fila in reader:
        vuelos.append(fila[0])

# Leer números de pista
pistas = []

with open("Data1k/pistas.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for fila in reader:
        pistas.append(int(fila[0]))   # numero_pista

usos = set()

with open("Data1k/usa_pista.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    while len(usos) < TOTAL_USOS:

        codigo_vuelo = random.choice(vuelos)
        numero_pista = random.choice(pistas)

        if (codigo_vuelo, numero_pista) not in usos:

            usos.add((codigo_vuelo, numero_pista))

            writer.writerow([
                codigo_vuelo,
                numero_pista
            ])

            if len(usos) % 100000 == 0:
                print(f"Generados: {len(usos):,} registros")

print(f"\nSe generaron {TOTAL_USOS:,} registros en usa_pista.csv.")