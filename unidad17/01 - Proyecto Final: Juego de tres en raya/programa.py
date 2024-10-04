from random import randrange


def MostrarTablero(tablero):
    print("+-------" * 3,"+", sep="")
    for fila in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(tablero[fila][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")


def IntroducirMovimiento(tablero):
    ok = False	# suposición falsa - la necesitamos para entrar en el bucle
    while not ok:
        try:
            movimiento = int(input("Ingresa tu movimiento: "))
        except:
            print("Movimiento erróneo, ingrésalo nuevamente")
            continue
        if not (movimiento >= 1 and movimiento <=9):  
            print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. ingrésalo nuevamente
            continue
        movimiento = movimiento - 1 	# numero de la celda, del 0 al 8
        fila = movimiento // 3 	# fila de la celda
        col = movimiento % 3		# columna de la celda
        signo = tablero[fila][col]	# marca el cuadro elegido
        ok = signo not in ['O','X'] 
        if not ok:	# esta ocupado, ingresa una posición nuevamente
            print("¡Cuadro ocupado, ingresa nuevamente!")
            continue
    tablero[fila][col] = 'O' 	# colocar '0' al cuadro seleccionado


def ListaCasillasLibres(tablero):
    libre = []	# la lista esta vacía inicialmente
    for fila in range(3): # itera a través de las filas
        for col in range(3): # itera a través de las columnas
            if tablero[fila][col] not in ['O','X']: # ¿Está la celda libre?
                libre.append((fila,col)) # si, agrega una nueva tupla a la lista
    return libre


def VictoriaPara(tablero,signo):
    if signo == "X":	# ¿Estamos buscando signo X?
        jugador = 'me'	# Si, es la maquina
    elif signo == "O": # ... ¿o estamos buscando O?
        jugador = 'you'	# Si, es el ussignoio
    else:
        jugador = None	# ¡No debemos de caer aquí!
    diagonal1 = diagonal2 = True  # para las diagonales
    for rc in range(3):
        if tablero[rc][0] == signo and tablero[rc][1] == signo and tablero[rc][2] == signo:	# check fila rc
            return jugador
        if tablero[0][rc] == signo and tablero[1][rc] == signo and tablero[2][rc] == signo: # check column rc
            return jugador
        if tablero[rc][rc] != signo: # revisar la primer diagonal
            diagonal1 = False
        if tablero[rc][2 - rc] != signo: # revisar la segunda diagonal
            diagonal2 = False
    print(diagonal1,diagonal2)
    if diagonal1 or diagonal2:
        return jugador
    return None


def DibujaMovimiento(tablero):
    libres = ListaCasillasLibres(tablero) # crea una lista de los cuadros vacios o libres
    cnt = len(libres)
    if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla
        this = randrange(cnt)
        fila, col = libres[this]
        tablero[fila][col] = 'X'


tablero = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
tablero[1][1] = 'X' # colocar la primer 'X' en el centro
libres = ListaCasillasLibres(tablero)
turno_humano = True # ¿De quien es turno ahora?
while len(libres):
    MostrarTablero(tablero)
    if turno_humano:
        IntroducirMovimiento(tablero)
        victor = VictoriaPara(tablero,'O')
    else:	
        DibujaMovimiento(tablero)
        victor = VictoriaPara(tablero,'X')
    if victor != None:
        break
    turno_humano = not turno_humano		
    libres = ListaCasillasLibres(tablero)


MostrarTablero(tablero)
if victor == 'you':
    print("¡Has ganado!")
elif victor == 'me':
    print("¡He ganado!")
else:
    print("¡Empate!")
