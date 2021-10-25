sueldos=[]
for x in range(5):
    v=int(input("Ingrese sueldo: "))
    sueldos.append(v)
print("Lista sin  ordenar: ")
print(sueldos)
for x in range(4):
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x]
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux
print("Lista ordenada: ")
print(sueldos)