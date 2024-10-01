tabla = []
num_filas=3
num_columnas=3
for f in range(num_filas):
    new_fila = []
    for c in range(num_columnas):
        print("Introduce el elemento que estará en la posición ",f,"-",c,":")
        elemento = int(input())
        new_fila.append(elemento)
    tabla.append(new_fila)
print(tabla)
