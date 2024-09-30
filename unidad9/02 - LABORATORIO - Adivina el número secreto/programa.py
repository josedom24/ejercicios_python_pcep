numero_secreto = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input("Adivina el número secreto:"))

while numero!=numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero = int(input("Adivina el número secreto:"))
print("¡Bien hecho, muggle! Eres libre ahora")
print("El número secreto es:",numero_secreto)