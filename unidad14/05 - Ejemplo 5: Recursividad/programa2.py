def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial(n - 1)

for n in range(1, 6):  # probando
    print(n, factorial(n))
