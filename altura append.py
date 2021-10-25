i=0
list=[]
contadormenor=0
contadormayor=0
suma=0
for n in range(5):
    a=float(input("Dame tu altura: "))
    list.append(a)
    suma=suma+a
promedio=suma//5

while i<len(list):
    if list[i]>promedio:
        contadormayor=contadormayor+1
    else:
        if list[i]<promedio:
            contadormenor=contadormenor+1
    i=i+1
print("Las  alturas son: ")
print(list)
print("El promedio es: ")
print(promedio)
print("Las personas mayores al promedio son: ")
print(contadormayor)
print("Las personas menores al promedio son: ")
print(contadormenor)