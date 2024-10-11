habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Indicamos como ocupadas algunas habitaciones del piso 15 del tercer edificio

habitaciones[2][14][0] = True
habitaciones[2][14][1] = True
habitaciones[2][14][2] = True

for edificio in habitaciones:
    for pisos in edificio:
        for habitacion in pisos:
            if habitacion:
                print("O ",end="")
            else:
                print("L ",end="")
        print()
    print("***********")
