producto=[]
precio=[]
contador=0
for x in range(5):
    p=(input("Ingrese el nombre del producto: "))
    producto.append(p)
    p2=int(input("Ingrese su precio: "))
    precio.append(p2)
for x in range(5):
    if precio[x]>precio[0]:
        contador=contador+1
print("El  número total de productos que superan el primero es de: ", contador)