my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for elem in my_list:
    if elem not in new_list:
        new_list.append(elem)
my_list=new_list[:]
print("La lista con elementos únicos:")
print(my_list)
