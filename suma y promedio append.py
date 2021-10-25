suma=0
list=[]
contador=0
for x in range(5):
    s=float(input("Dame tu sueldo: "))
    list.append(s)
    suma=suma+s
print("Los sueldos son: ")
print(list)
promedio=suma//5
print("El promedio es: ")
print(promedio)