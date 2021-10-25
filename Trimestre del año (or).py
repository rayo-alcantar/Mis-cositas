m=int(input("Número del mes"))
d=int(input("Número del día"))
a=int(input("Número del año"))
if m==1 or m==2 or m==3:
    print("La fecha: ")
    print( d, ", ",  m, ", ",  a)
    print("Corresponde   al primer trimestre del año")
else:
    print("La fecha: ")
    print(d, ", ", m, ", ", a)
    print("No corresponde  al primer trimestre del año")