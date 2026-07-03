# ==========================================================
# Generador de datos para la tabla VUELO.
#
# Atributos:
# - codigo_vuelo (PK)
# - codigo_icao (FK -> AEROLINEA)
# - origen
# - destino
# - fecha
# - hora_salida
# - hora_llegada
# - estado
# ==========================================================

import csv
import os
import random
from datetime import datetime, timedelta

TOTAL_VUELOS = 1_000

os.makedirs("Data10k", exist_ok=True)

icaos = []

with open("Data1k/aerolineas.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        icaos.append(fila[0])

aeropuertos = [
    "LIM","CUZ","AQP","PIU","TRU","IQT","JUL","TCQ",
    "SCL","EZE","MVD","GRU","GIG","BOG","UIO","MEX",
    "JFK","LAX","MIA","ORD","ATL","MAD","BCN","CDG",
    "FCO","LHR","FRA","NRT","ICN","SYD","YYZ"
]

otros_aeropuertos = [a for a in aeropuertos if a != "LIM"]

estados = [
    "Programado",
    "Abordando",
    "En vuelo",
    "Retrasado",
    "Cancelado",
    "Finalizado"
]

codigos = set()

with open("Data1k/vuelos.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_VUELOS):

        codigo_icao = random.choice(icaos)

        while True:
            numero = random.randint(1, 9999)
            codigo_vuelo = f"{codigo_icao}{numero:04d}"

            if codigo_vuelo not in codigos:
                codigos.add(codigo_vuelo)
                break

        if random.random() < 0.5:
            origen = "LIM"
            destino = random.choice(otros_aeropuertos)
        else:
            origen = random.choice(otros_aeropuertos)
            destino = "LIM"

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

        fecha = salida.strftime("%Y-%m-%d")
        hora_salida = salida.strftime("%H:%M:%S")
        hora_llegada = llegada.strftime("%H:%M:%S")

        writer.writerow([
            codigo_vuelo,
            codigo_icao,
            origen,
            destino,
            fecha,
            hora_salida,
            hora_llegada,
            estado
        ])

        if (i + 1) % 100000 == 0:
            print(f"Generados: {i + 1:,} vuelos")

print(f"\nSe generaron {TOTAL_VUELOS:,} vuelos correctamente.")