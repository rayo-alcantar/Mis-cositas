list=[]
for x in range(5):
    v=int(input("Ingrese valor: "))
    list.append(v)
mayor=list[0]
for x in range(1,5):
    if list[x]>mayor:
        mayor=list[x]
print("Lista completa: ")
print(list)
print("Mayor de la lista: ")
print(mayor)