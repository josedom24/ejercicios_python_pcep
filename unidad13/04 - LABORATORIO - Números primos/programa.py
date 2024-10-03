def es_primo(num):
    for numero in range(2,num):
        if num % numero == 0:
            return False
    return True

for i in range(1, 20):
    if es_primo(i + 1):
            print(i + 1, end=" ")
print()