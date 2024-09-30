# Modifica el programa anterior para que no pida el número por teclado, 
# sino que muestre las tablas de multiplicas de los 5 primeros números.
for tabla in range(1,6):
	for num in range(1, 11):
		print(num,"*", tabla,"=",num*tabla)
	print()
