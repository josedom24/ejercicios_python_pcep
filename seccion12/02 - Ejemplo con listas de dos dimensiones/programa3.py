import random

num_filas = 31
num_columnas = 24
temperaturas = [[0.0 for h in range(24)] for d in range(31)]

# Actualizamos las temperaturas, con valores aleatorios.

for dia in range(num_filas):
    for hora in range(num_columnas):
        temperaturas[dia][hora] = round(random.uniform(0, 40), 1)

# Calculamos la cantidad de días en que las temperatura al mediodía fue menor que 20 ºC.


dias_calurosos = 0

temp_mas_alta = -100.0

for temp_en_dia in temperaturas:
    if temp_en_dia[11]>20:
        dias_calurosos += 1
        
print(dias_calurosos, "fueron los días calurosos.")
