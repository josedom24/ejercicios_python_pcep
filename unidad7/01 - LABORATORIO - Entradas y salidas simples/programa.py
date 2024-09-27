# Pedimos que se introduzcan los números
numero1 = float(input("Introduce el número 1:"))
numero2 = float(input("Introduce el número 1:"))

# Realizamos los cálculos

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Mostramos los resultados

print("Suma:",suma)
print("Resta:",resta)
print("Multiplicación:",multiplicacion)
print("División:",division)

# Otra forma de mostrar los resultados sin usar las variables intermedias
print(20 * "-")
print("Suma:",numero1 + numero2)
print("Resta:",numero1 - numero2)
print("Multiplicación:",numero1 * numero2)
print("División:",numero1 / numero2)

# Otra forma de mostrar los resultados convertiendo los resultados a cadenas

print(20 * "-")
print("Suma: " + str(numero1 + numero2))
print("Resta: " + str(numero1 - numero2))
print("Multiplicación: " + str(numero1 * numero2))
print("División: " + str(numero1 / numero2))
