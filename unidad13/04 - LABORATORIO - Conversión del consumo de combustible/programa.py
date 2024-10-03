def litros_100km_a_millas_galon(litros):
    galon = 3.785411784   # litros por galón
    milla = 1609.344    # metros por milla
    kpg = (galon / milla * 1000)    # kilómetros por galón
    return  100 / litros * kpg    # devuelve el combustible como mpg 


def millas_galon_a_litros_100km(millas):
    galon = 3.785411784   # litros por galón
    milla = 1609.344    # metros por milla
    kpg = (galon / milla * 1000)    # kilómetros por galón
    return  100 / millas * kpg    # devuelve el combustible como l/100km 

print(litros_100km_a_millas_galon(3.9))
print(litros_100km_a_millas_galon(7.5))
print(litros_100km_a_millas_galon(10.))


print(millas_galon_a_litros_100km(60.3))
print(millas_galon_a_litros_100km(31.4))
print(millas_galon_a_litros_100km(23.5))