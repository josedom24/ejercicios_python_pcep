palabra_sin_vocales = ""
palabra_usuario = input("Introduce una palabra:")
palabra_usuario = palabra_usuario.upper()
for letra in palabra_usuario:
    if letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        continue
    palabra_sin_vocales += letra
print(palabra_sin_vocales)