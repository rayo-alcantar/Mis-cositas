list=[]
temp=0
x=0
e=int(input("Cuantos empleados tiene la empresa?"))
while x<e:
    temp=int(input("Dame sueldo: "))
    list.append(temp)
    x=x+1
print("Lista sin ordenar: ")
print(list)
for k in range(e):
    for i in range(e-1):
        if list[i]>list[i+1]:
            aux=list[i]
            list[i]=list[i+1]
            list[i+1]=aux
print("Lista ordenada de menor a mayor:")
print(list)