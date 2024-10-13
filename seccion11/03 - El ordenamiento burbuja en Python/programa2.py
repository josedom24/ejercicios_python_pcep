my_list = []
intercambio = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while intercambio:
    intercambio = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            intercambio = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)
