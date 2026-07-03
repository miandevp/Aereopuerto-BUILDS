# ==========================================================
# Generador de datos para la tabla ASIGNADO.
#
# Atributos:
# - codigo_vuelo (FK -> VUELO)
# - numero_embarque (FK -> PUERTA_EMBARQUE)
#
# Relaciona los vuelos con las puertas de embarque.
#
# Cambiar TOTAL_ASIGNACIONES para generar distintos tamaños:
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

TOTAL_ASIGNACIONES = 2_000_000

os.makedirs("Data", exist_ok=True)

# Leer los códigos de vuelo existentes
vuelos = []

with open("Data/vuelos.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        vuelos.append(fila[0])

# Leer los números de puerta existentes
puertas = []

with open("Data/puertas_embarque.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        puertas.append(int(fila[0]))

# Evitar relaciones repetidas
asignaciones = set()

with open("Data/asignado.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    while len(asignaciones) < TOTAL_ASIGNACIONES:

        codigo_vuelo = random.choice(vuelos)
        numero_puerta = random.choice(puertas)

        if (codigo_vuelo, numero_puerta) not in asignaciones:

            asignaciones.add((codigo_vuelo, numero_puerta))

            writer.writerow([
                codigo_vuelo,
                numero_puerta
            ])

            if len(asignaciones) % 100000 == 0:
                print(f"Generadas: {len(asignaciones):,} asignaciones")

print(f"\nSe generaron {TOTAL_ASIGNACIONES:,} asignaciones correctamente.")