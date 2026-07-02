# ==========================================================
# Generador de datos para la tabla AVION.
#
# Atributos:
# - matricula (PK)
# - codigo_icao (FK -> AEROLINEA)
# - modelo
# - capacidad
# - anio_fabricacion
#
# El código ICAO debe existir previamente en la tabla
# AEROLINEA.
#
# Por realismo, la cantidad de aviones permanece fija,
# ya que en un sistema aeroportuario no existen millones
# de aeronaves.
#
# Cantidad de aviones:
# 10_000
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random

TOTAL_AVIONES = 10_000

os.makedirs("Data", exist_ok=True)

# Leer todos los códigos ICAO existentes
icaos = []

with open("Data/aerolineas.csv", "r", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        icaos.append(fila[0])

modelos = [
    ("Airbus A220", 150),
    ("Airbus A319", 140),
    ("Airbus A320", 180),
    ("Airbus A321", 220),
    ("Airbus A330", 300),
    ("Airbus A350", 350),
    ("Airbus A380", 520),
    ("Boeing 737-700", 140),
    ("Boeing 737-800", 189),
    ("Boeing 737 MAX 8", 210),
    ("Boeing 757", 239),
    ("Boeing 767", 280),
    ("Boeing 777", 396),
    ("Boeing 787 Dreamliner", 330),
    ("Embraer E175", 88),
    ("Embraer E190", 114),
    ("ATR 72", 72),
    ("Bombardier CRJ900", 90)
]

matriculas = set()

with open("Data/aviones.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_AVIONES):

        # Matrícula única
        while True:
            matricula = (
                random.choice(["N", "OB", "EC", "LV", "CC", "PT"])
                + "-"
                + "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))
            )

            if matricula not in matriculas:
                matriculas.add(matricula)
                break

        codigo_icao = random.choice(icaos)

        modelo, capacidad = random.choice(modelos)

        anio_fabricacion = random.randint(1995, 2025)

        writer.writerow([
            matricula,
            codigo_icao,
            modelo,
            capacidad,
            anio_fabricacion
        ])

        if (i + 1) % 1000 == 0:
            print(f"Generados: {i + 1:,} aviones")

print(f"\nSe generaron {TOTAL_AVIONES:,} aviones correctamente.")