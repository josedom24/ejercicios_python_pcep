def es_un_triangulo(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(es_un_triangulo(1, 1, 1))
print(es_un_triangulo(1, 1, 3))
