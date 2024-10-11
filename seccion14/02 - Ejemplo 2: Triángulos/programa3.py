def es_un_triangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(es_un_triangulo(1, 1, 1))
print(es_un_triangulo(1, 1, 3))
