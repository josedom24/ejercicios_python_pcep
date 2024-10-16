alumnos = {}

nombre = input("Ingresa el nombre del estudiante: ")
while nombre != "":

    nota = int(input("Ingresa la calificación del estudiante (0-10): "))
    if nota not in range(0, 11):
	    break
    
    if nombre in alumnos:
        alumnos[nombre] += (nota,)
    else:
        alumnos[nombre] = (nota,)
    nombre = input("Ingresa el nombre del estudiante: ")
        
for nombre in sorted(alumnos.keys()):
    total = 0
    contador = 0
    for nota in alumnos[nombre]:
        total += nota
        contador += 1
    print(nombre, ":", total / contador)
