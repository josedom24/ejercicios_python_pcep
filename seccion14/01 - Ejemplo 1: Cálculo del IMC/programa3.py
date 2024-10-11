def pie_pulgada_a_metro(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def libra_a_kg(lb):
    return lb * 0.45359237


def imc(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(imc(weight = libra_a_kg(176), height = pie_pulgada_a_metro(5, 7)))