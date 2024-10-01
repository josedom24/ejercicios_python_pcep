loteria = [5, 11, 9, 42, 3, 49]
tus_numeros = [3, 7, 11, 42, 34, 49]
hits = 0

for number in tus_numeros:
    if number in loteria:
        hits += 1

print(hits)
