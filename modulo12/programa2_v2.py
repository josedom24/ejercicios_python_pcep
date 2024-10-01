my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
indice = 0
for i in my_list:
    found = i == to_find
    if found:
        break
    indice+=1

if found:
    print("Elemento encontrado en el índice", indice)
else:
    print("ausente")
