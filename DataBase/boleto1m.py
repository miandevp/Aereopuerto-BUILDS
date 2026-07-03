# ==========================================================
# Generador de datos para la tabla BOLETO.
#
# Atributos:
# - id_boleto (PK)
# - precio
# - codigo_vuelo (FK -> VUELO)
#
# Cambiar TOTAL_BOLETOS para generar distintos tamaños:
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

TOTAL_BOLETOS = 2_000_000

os.makedirs("Data", exist_ok=True)

# Leer todos los códigos de vuelo existentes
codigos_vuelo = []

with open("Data/vuelos.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        codigos_vuelo.append(fila[0])

with open("Data/boletos.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_BOLETOS):

        id_boleto = i + 1

        # Precio entre S/ 80 y S/ 1800
        precio = random.randint(80, 1800)

        codigo_vuelo = random.choice(codigos_vuelo)

        writer.writerow([
            id_boleto,
            codigo_vuelo,
            precio
        ])

        if (i + 1) % 100000 == 0:
            print(f"Generados: {i + 1:,} boletos")

print(f"\nSe generaron {TOTAL_BOLETOS:,} boletos correctamente.")