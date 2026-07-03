# ==========================================================
# Generador de datos para la tabla PASAJERO.
#
# Atributos:
# - dni_pasajero (PK)
# - nombre
# - apellido
# - telefono
# - nacionalidad
#
# El DNI es la clave primaria y debe ser único para
# identificar a cada pasajero.
#
# Cambiar TOTAL_PASAJEROS para generar distintos tamaños:
# 1_000
# 10_000
# 100_000
# 1_000_000
#
# En este proyecto se generan 2 millones de pasajeros.
#c
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random
from faker import Faker

TOTAL_PASAJEROS = 1_000

os.makedirs("Data1k", exist_ok=True)

fake = Faker([
    "es_ES",
    "en_US",
    "pt_BR",
    "fr_FR",
    "de_DE",
    "it_IT",
    "ja_JP"
])

nacionalidades = [
    "Peruana",
    "Argentina",
    "Boliviana",
    "Brasileña",
    "Chilena",
    "Colombiana",
    "Ecuatoriana",
    "Uruguaya",
    "Paraguaya",
    "Venezolana",
    "Mexicana",
    "Estadounidense",
    "Canadiense",
    "Española",
    "Francesa",
    "Italiana",
    "Alemana",
    "Británica",
    "Portuguesa",
    "Neerlandesa",
    "Belga",
    "Suiza",
    "Sueca",
    "Noruega",
    "Danesa",
    "Finlandesa",
    "Rusa",
    "China",
    "Japonesa",
    "Coreana",
    "India",
    "Australiana",
    "Neozelandesa",
    "Sudafricana",
    "Egipcia"
]

with open("Data1k/pasajeros.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for i in range(TOTAL_PASAJEROS):

        dni_pasajero = str(70000000 + i)
        nombre = fake.first_name()
        apellido = fake.last_name()
        telefono = fake.msisdn()[-9:]
        nacionalidad = random.choice(nacionalidades)

        writer.writerow([
            dni_pasajero,
            nombre,
            apellido,
            nacionalidad,
            telefono
        ])

        if (i + 1) % 100000 == 0:
            print(f"Generados: {i + 1:,} pasajeros")

print(f"\nSe generaron {TOTAL_PASAJEROS:,} pasajeros correctamente.")