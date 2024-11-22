import random

num_filas = 31
num_columnas = 24
temperaturas = [[0.0 for h in range(24)] for d in range(31)]

# Actualizamos las temperaturas, con valores aleatorios.

for dia in range(num_filas):
    for hora in range(num_columnas):
        temperaturas[dia][hora] = round(random.uniform(0, 40), 1)

# Calculamos la temperatura media del mes al mediodía

total = 0.0

for temp_en_dia in temperaturas:
    total += temp_en_dia[11]

media = total / 31

print("Temperatura promedio al mediodía:", media)

