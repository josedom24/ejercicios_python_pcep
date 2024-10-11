def es_un_triangulo(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(es_un_triangulo(1, 1, 1))
print(es_un_triangulo(1, 1, 3))
