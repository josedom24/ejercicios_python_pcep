# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
print("Introduce a los siguiente miembros de los Beatles: Stu Sutcliffe y Pete Best")
for i in range(2):
    beatles.append(input("Introduce miembro de los Beatles:"))
print("Paso 3:", beatles)

# paso 4
del beatles[3]
del beatles[3]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Número de Beatles:", len(beatles))