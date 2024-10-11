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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = dias_del_mes(yr, mo)
    print(result)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")