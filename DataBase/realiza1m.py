# ==========================================================
# Generador de datos para la tabla REALIZA.
#
# Atributos:
# - codigo_vuelo (FK -> VUELO)
# - matricula (FK -> AVION)
#
# Relaciona cada vuelo con un avión.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import random
import os

os.makedirs("Data1k", exist_ok=True)

# Leer todas las matrículas de los aviones
matriculas = []

with open("Data1k/aviones.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        matriculas.append(fila[0])

contador = 0

with open("Data1k/vuelos.csv", encoding="utf-8") as vuelos, \
     open("Data1k/realiza.csv", "w", newline="", encoding="utf-8") as salida:

    reader = csv.reader(vuelos)
    writer = csv.writer(salida)

    for fila in reader:

        codigo_vuelo = fila[0]
        matricula = random.choice(matriculas)

        writer.writerow([
            codigo_vuelo,
            matricula
        ])

        contador += 1

        if contador % 100000 == 0:
            print(f"Generados: {contador:,} relaciones")

print(f"\nSe generaron {contador:,} registros en realiza.csv.")