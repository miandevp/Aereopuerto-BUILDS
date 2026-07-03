# ==========================================================
# Generador de datos para la tabla ASIGNADO.
#
# Atributos:
# - id_area (PK, FK -> AREA.id_area)
# - dni_empleado (FK -> EMPLEADO.dni_empleado)
#
# El archivo CSV se genera SIN CABECERA.
# ==========================================================

import csv
import os
import random

os.makedirs("Data1k", exist_ok=True)

# Leer todas las áreas
areas = []

with open("Data1k/areas.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        areas.append(fila[0])   # id_area

# Leer todos los empleados
empleados = []

with open("Data1k/empleados.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for fila in reader:
        empleados.append(fila[0])   # dni_empleado

with open("Data1k/asignado_empleado.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i, id_area in enumerate(areas):

        dni_empleado = random.choice(empleados)

        writer.writerow([
            id_area,
            dni_empleado
        ])

        if (i + 1) % 100 == 0:
            print(f"Generados: {i + 1:,} asignados")

print(f"\nSe generaron {len(areas):,} asignaciones correctamente.")