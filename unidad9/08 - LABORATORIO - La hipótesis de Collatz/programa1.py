c0=int(input("Introduce un número:"))

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 +1
    print(c0)
    