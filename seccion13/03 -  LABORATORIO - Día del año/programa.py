def año_bisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True

def dias_del_mes(año, mes):
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    dias_mes = 0
    if mes < 0 or mes>12:
        return None
    dias_mes = dias[mes - 1]
    if mes==2 and año_bisiesto(año):
        dias_mes += 1
    return dias_mes

def dia_del_año(año, mes, dia):
    dia_año = 0
    if (mes < 0 or mes>12) or (dia< 0 or dia>dias_del_mes(año,mes)):
        return None
    for mes_actual in range(1, mes):
        print(dias_del_mes(año,mes_actual))
        dia_año += dias_del_mes(año,mes_actual)
    dia_año += dia
    return dia_año

print(dia_del_año(2000, 12, 31))