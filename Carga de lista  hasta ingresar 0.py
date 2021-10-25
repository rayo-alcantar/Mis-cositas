list=[]
v=int(input("Dame un valor, y añade 0 para terminar: "))
while v!=0:
    list.append(v)
    v=int(input("Dame un valor, y añade 0 para terminar: "))
print("Tamaño de lalista: ")
print(len(list))