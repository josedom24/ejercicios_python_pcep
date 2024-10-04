from math import pi   # Usamos el valor de pi del módulo matemático math

def mostrar_resultado(mensaje,valor):
    print(mensaje,valor)

radio = input("Introduce el radio: ")
altura = input("Introduce la altura: ")
conovol = 1/3*pi*radio*2*altura   # Volumen del cono
cilvol = pi*radio**2*altura        # Volumen del cilindro
esferavol = 3/4*pi*radio**3        # Volumen de la esfera
mostrar_resultado("El volumen del cono:", conovol)
mostrar_resultado("El volumen del cilindro:", cilvol)
mostrar_resultado("El volumen de la esfera:", esferavol)
