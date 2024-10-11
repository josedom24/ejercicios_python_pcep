import random

num_filas = 31
num_columnas = 24
temperaturas = [[0.0 for h in range(24)] for d in range(31)]

# Actualizamos las temperaturas, con valores aleatorios.

for dia in range(num_filas):
    for hora in range(num_columnas):
        temperaturas[dia][hora] = round(random.uniform(0, 40), 1)

# Calculamos la temperatura más alta
temp_mas_alta = -100.0

for temp_en_dia in temperaturas:
    for temp in temp_en_dia:
        if temp > temp_mas_alta:
            temp_mas_alta = temp

print("La temperatura más alta fue:", temp_mas_alta)
