# ==========================================================
# Generador de datos para la tabla EMPLEADO.
#
# Atributos:
# - dni_empleado (PK)
# - nombre
# - apellido
# - cargo
# - turno
#
# Cambiar TOTAL_EMPLEADOS para generar distintos tamaños:
# 1_000
# 10_000
# 100_000
#
# En este proyecto se generan 100,000 empleados.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random
from faker import Faker

TOTAL_EMPLEADOS = 1_000

fake = Faker("es_ES")

os.makedirs("Data1k", exist_ok=True)

cargos = [
    "Piloto",
    "Copiloto",
    "Azafata",
    "Tripulante",
    "Mecanico",
    "Supervisor",
    "Controlador Aereo",
    "Agente de Check-in",
    "Agente de Embarque",
    "Seguridad",
    "Administrador",
    "Gerente",
    "Despachador",
    "Tecnico",
    "Operario"
]

turnos = [
    "Mañana",
    "Tarde",
    "Noche"
]

dnis = set()

with open("Data1k/empleados.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_EMPLEADOS):

        while True:
            dni = str(random.randint(72000000, 72999999))
            if dni not in dnis:
                dnis.add(dni)
                break

        nombre = fake.first_name()
        apellido = fake.last_name()
        cargo = random.choice(cargos)
        turno = random.choice(turnos)

        writer.writerow([
            dni,
            nombre,
            apellido,
            cargo,
            turno
        ])

        if (i + 1) % 10000 == 0:
            print(f"Generados: {i + 1:,} empleados")

print(f"\nSe generaron {TOTAL_EMPLEADOS:,} empleados correctamente.")