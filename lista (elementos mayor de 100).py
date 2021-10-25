list=[101, 202, 323, 3223, 3212, 2, 11111111]
x=0
contador=0
while x<len(list):
    if list[x]>100:
        contador=contador+1
    x=x+1
print("El total de elementos mayor a 100 es de: ", contador)