# ==========================================================
# Generador de datos para la tabla AREA_COMERCIAL.
#
# Atributos:
# - id_area (PK, FK -> AREA)
#
# Se utilizan los id_area existentes del 1 al 250.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os

os.makedirs("Data", exist_ok=True)

with open("Data/areas.csv", encoding="utf-8") as padre, \
     open("Data/area_comercial.csv", "w", newline="", encoding="utf-8") as salida:

    reader = csv.reader(padre)
    writer = csv.writer(salida)

    for fila in reader:

        id_area = int(fila[0])

        # Área Comercial: IDs del 1 al 250
        if 1 <= id_area <= 250:
            writer.writerow([id_area])

print("Área Comercial generada correctamente.")