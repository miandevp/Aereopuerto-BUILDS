# ==========================================================
# Generador de datos para la tabla VUELO.
#
# Atributos:
# - codigo_vuelo (PK)
# - codigo_icao (FK -> AEROLINEA)
# - origen
# - destino
# - estado
# - hora_salida
# - hora_llegada
#
# El código ICAO debe existir previamente en la tabla
# AEROLINEA.
#
# Cambiar TOTAL_VUELOS para generar distintos tamaños:
# 1_000
# 10_000
# 100_000
# 1_000_000
#
# En este proyecto se generan 2 millones de vuelos.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random
from datetime import datetime, timedelta

TOTAL_VUELOS = 2_000_000

os.makedirs("Data", exist_ok=True)

# Leer códigos ICAO existentes
icaos = []

with open("Data/aerolineas.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for fila in reader:
        icaos.append(fila[0])

aeropuertos = [
    "LIM","CUZ","AQP","PIU","TRU","IQT","JUL","TCQ",
    "SCL","EZE","MVD","GRU","GIG","BOG","UIO","MEX",
    "JFK","LAX","MIA","ORD","ATL","MAD","BCN","CDG",
    "FCO","LHR","FRA","NRT","ICN","SYD","YYZ"
]

estados = [
    "Programado",
    "Abordando",
    "En vuelo",
    "Retrasado",
    "Cancelado",
    "Finalizado"
]

codigos = set()

with open("Data/vuelos.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_VUELOS):

        codigo_icao = random.choice(icaos)

        while True:
            numero = random.randint(1, 9999)
            codigo_vuelo = f"{codigo_icao}{numero:04d}"

            if codigo_vuelo not in codigos:
                codigos.add(codigo_vuelo)
                break

        origen = random.choice(aeropuertos)

        destino = random.choice(aeropuertos)
        while destino == origen:
            destino = random.choice(aeropuertos)

        estado = random.choice(estados)

        salida = datetime(
            2024,
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(0, 23),
            random.choice([0, 15, 30, 45])
        )

        llegada = salida + timedelta(
            hours=random.randint(1, 15),
            minutes=random.randint(0, 59)
        )

        writer.writerow([
            codigo_vuelo,
            codigo_icao,
            origen,
            destino,
            estado,
            salida.strftime("%Y-%m-%d %H:%M"),
            llegada.strftime("%Y-%m-%d %H:%M")
        ])

        if (i + 1) % 100000 == 0:
            print(f"Generados: {i + 1:,} vuelos")

print(f"\nSe generaron {TOTAL_VUELOS:,} vuelos correctamente.")