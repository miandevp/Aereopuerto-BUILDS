# ==========================================================
# Generador de datos para la tabla EQUIPAJE.
#
# Atributos:
# - id_boleto (PK, FK -> BOLETO)
# - nro_equipaje (PK)
# - id_area (FK -> AREA_EQUIPAJE)
# - peso_kg
# - dimension
# - estado
#
# Se genera entre 0 y 2 equipajes por boleto.
#
# El archivo CSV se genera SIN CABECERA.
# ==========================================================

import csv
import os
import random

os.makedirs("Data1k", exist_ok=True)

# Leer boletos
boletos = []

with open("Data1k/boletos.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        boletos.append(int(fila[0]))

# Leer áreas de equipaje
areas = []

with open("Data1k/area_equipaje.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        areas.append(int(fila[0]))

estados = [
    "Registrado",
    "En tránsito",
    "Entregado",
    "Extraviado"
]

dimensiones = [
    "Pequeño",
    "Mediano",
    "Grande"
]

contador = 0

with open("Data1k/equipajes.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for id_boleto in boletos:

        # Cada boleto puede tener entre 0 y 2 equipajes
        cantidad = random.randint(0, 2)

        for nro_equipaje in range(1, cantidad + 1):

            id_area = random.choice(areas)
            peso_kg = round(random.uniform(5, 32), 2)
            dimension = random.choice(dimensiones)
            estado = random.choice(estados)

            writer.writerow([
                id_boleto,
                nro_equipaje,
                id_area,
                peso_kg,
                dimension,
                estado
            ])

            contador += 1

            if contador % 100000 == 0:
                print(f"Generados: {contador:,} equipajes")

print(f"\nSe generaron {contador:,} equipajes correctamente.")