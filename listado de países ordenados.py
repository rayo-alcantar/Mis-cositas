paises=[]
for x in range(5):
    p=(input("Escribe un país: "))
    paises.append(p)
print("Lista sin ordenar: ")
print(paises)
for k in range(4):
    for x in range(4):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
print("Lista ordenada: ")
print(paises)