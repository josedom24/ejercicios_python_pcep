habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Indicamos como ocupadas algunas habitaciones del piso 15 del tercer edificio

habitaciones[2][14][0] = True
habitaciones[2][14][1] = True
habitaciones[2][14][2] = True

disponibilidad = 0

for num_habitacion in range(20):
    if not habitaciones[2][14][num_habitacion]:
        disponibilidad += 1
print("Hay disponibles",disponibilidad,"habitaciones en el piso 15 del edificio número 3.")
