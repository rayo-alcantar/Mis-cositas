cantidad=0
n=int(input("Cuantos valores ingresará?"))
for x in range(n):
    v=int(input("Ingrese valor"))
    if v>=100:
        cantidad=cantidad+1
print("La cantidad de números iguales o mayores a 1000  son: ")
print(cantidad)