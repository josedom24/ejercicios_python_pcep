# Con while
cont = 0
while cont<10:
    cont = cont + 1
    if cont % 2 != 0:
        continue
    print(cont)

# Con for
for cont in range(1,11):
    if cont % 2 != 0:
        continue
    print(cont)
