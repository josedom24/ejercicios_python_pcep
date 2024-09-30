altura = 0
bloques = int(input("Ingresa el número de bloques: "))
bloque_por_fila = 1

while bloques >= bloque_por_fila:
    altura += 1
    bloques = bloques - bloque_por_fila
    bloque_por_fila += 1

print("La altura de la pirámide:", altura)