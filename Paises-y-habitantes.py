paises=[]
habitantes=[]
for x in range(5):
    p=(input("Nombre del país: "))
    paises.append(p)
    ha=int(input("Ingrese habitantes: "))
    habitantes.append(ha)
for k in range(4):
    for x in range(4):
        if paises[x]<paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2
print("La lista de países ordenada por alfabeto, de mayor a menor.")
for x in range(4):
    print(paises[x], habitantes[x])
print("Ahora los países  ordenados  con su población de mayor a menor: ")
for k in range(4):
    for x in range(4):
        if habitantes[x]<habitantes[x+1]:
            aux=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux
            aux2=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux2
for x in range(4):
    print(paises[x], habitantes[x])