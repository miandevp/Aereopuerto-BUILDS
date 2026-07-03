# ==========================================================
# Generador de datos para la tabla AEROLINEA.
#
# Atributos:
# - codigo_icao (PK)
# - nombre
# - pais_origen
# - telefono
#
# El código ICAO es la clave primaria y debe ser único.
#
# El archivo CSV se genera SIN CABECERA.
# Se guarda automáticamente en la carpeta Data/.
# ==========================================================

import csv
import os
import random
import string
from faker import Faker

fake = Faker()

TOTAL_AEROLINEAS = 1000

os.makedirs("Data", exist_ok=True)

paises = {
    "Perú": "+51",
    "Argentina": "+54",
    "Chile": "+56",
    "Colombia": "+57",
    "Ecuador": "+593",
    "Brasil": "+55",
    "México": "+52",
    "Estados Unidos": "+1",
    "Canadá": "+1",
    "España": "+34",
    "Francia": "+33",
    "Italia": "+39",
    "Reino Unido": "+44",
    "Alemania": "+49",
    "Japón": "+81",
    "Corea del Sur": "+82",
    "China": "+86",
    "Australia": "+61",
    "Uruguay": "+598",
    "Panamá": "+507"
}

codigos_usados = set()

with open("Data/aerolineas.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    for _ in range(TOTAL_AEROLINEAS):

        # Código ICAO único de 4 letras
        while True:
            codigo_icao = "".join(random.choices(string.ascii_uppercase, k=4))
            if codigo_icao not in codigos_usados:
                codigos_usados.add(codigo_icao)
                break

        pais = random.choice(list(paises.keys()))

        nombre = fake.company() + " Airlines"

        telefono = (
            paises[pais]
            + "".join(random.choices(string.digits, k=9))
        )

        writer.writerow([
            codigo_icao,
            nombre,
            pais,
            telefono
        ])

print(f"Se generaron {TOTAL_AEROLINEAS} aerolíneas correctamente.")