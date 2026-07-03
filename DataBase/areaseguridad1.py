# ==========================================================
# Generador de datos para la tabla AREA_SEGURIDAD.
#
# Atributos:
# - id_area (PK, FK -> AREA)
#
# Se utilizan los id_area existentes del 751 al 1000.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os

os.makedirs("Data", exist_ok=True)

with open("Data/areas.csv", encoding="utf-8") as padre, \
     open("Data/area_seguridad.csv", "w", newline="", encoding="utf-8") as salida:

    reader = csv.reader(padre)
    writer = csv.writer(salida)

    for fila in reader:

        id_area = int(fila[0])

        # Área Seguridad: IDs del 751 al 1000
        if 751 <= id_area <= 1000:
            writer.writerow([id_area])

print("Área Seguridad generada correctamente.")