aaprobado=0
reprobado=0
x=1
while x<=10:
    cal=float(input("Dame la calificación"))
    if cal >=6:
        aaprobado=aaprobado+1
    else:
        reprobado=reprobado+1
        x=x+1
print("Reprobados son: ")
print(reprobado)
print("Aprobados son: ")
print(aaprobado)