def es_un_triangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b


def es_un_triangulo_rectangulo(a, b, c):
    if not es_un_triangulo(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == c ** 2 + a ** 2


print(es_un_triangulo_rectangulo(5, 3, 4))
print(es_un_triangulo_rectangulo(1, 3, 4))
