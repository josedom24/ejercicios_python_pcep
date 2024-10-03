def es_un_triangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_triangulo(a, b, c):
    if not es_un_triangulo(a, b, c):
        return None
    return heron(a, b, c)


print(area_triangulo(1., 1., 2. ** .5))
