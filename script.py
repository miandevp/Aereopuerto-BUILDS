import csv
import random
import os

ARCHIVO_RESERVAS = "reservas.csv"
ARCHIVO_BOLETOS = "boletos.csv"
TEMP = "reservas.tmp"

# Leer todos los id_boleto
ids_boleto = []

with open(ARCHIVO_BOLETOS, "r", encoding="utf-8", newline="") as f:
    lector = csv.reader(f)
    for fila in lector:
        if fila:
            ids_boleto.append(fila[0])

random.shuffle(ids_boleto)

with open(ARCHIVO_RESERVAS, "r", encoding="utf-8", newline="") as fin, \
        open(TEMP, "w", encoding="utf-8", newline="") as fout:
    lector = csv.reader(fin)
    escritor = csv.writer(fout)

    i = 0

    for fila in lector:

        if i >= len(ids_boleto):
            break

        # Insertar id_boleto como tercera columna
        nueva_fila = [
            fila[0],  # id_reserva
            fila[1],  # dni_pasajero
            ids_boleto[i],  # id_boleto
            fila[2],  # estado
            fila[3],  # numero_asiento
            fila[4],  # fecha
            fila[5]  # clase
        ]

        escritor.writerow(nueva_fila)
        i += 1

os.remove(ARCHIVO_RESERVAS)
os.rename(TEMP, ARCHIVO_RESERVAS)

print("reservas.csv actualizado correctamente.")