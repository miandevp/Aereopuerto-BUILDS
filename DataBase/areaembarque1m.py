# ==========================================================
# Generador de datos para la tabla AREA_EMBARQUE.
#
# Atributos:
# - id_area (PK, FK -> AREA)
#
# Se utilizan los id_area existentes del 251 al 500.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os

os.makedirs("Data", exist_ok=True)

with open("Data/areas.csv", encoding="utf-8") as padre, \
     open("Data/area_embarque.csv", "w", newline="", encoding="utf-8") as salida:

    reader = csv.reader(padre)
    writer = csv.writer(salida)

    for fila in reader:

        id_area = int(fila[0])

        # Área Embarque: IDs del 251 al 500
        if 251 <= id_area <= 500:
            writer.writerow([id_area])

print("Área Embarque generada correctamente.")