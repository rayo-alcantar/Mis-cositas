list=[]
for x in range(5):
    n=(input("Dame el nombre: "))
    list.append(n)

menor=list[0]
for x in range(1,5):
    if list[x]<menor:
        menor=list[x]
print("Todos los nombres son: ", list)
print("El nombre menor es: ", menor)