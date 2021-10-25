list=[[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14]]
 print("Aquí la lista: ")
print(list)
print("Primer elemento: ")
print(list[0])
print("Primer elemento de la lista contenida: ")
print(list[0][0])
print("imprimimos con un for la lista contenida en la primer componente: ")
for x in range(len(list[0])):
    print(list[0][x])
