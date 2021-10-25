aprobados=0
reprobados=0
for x in range(10):
    n=int(input("Dame la nota: "))
    if n>=7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1
print("El número de aprobdados es de: ")
print(aprobados)
print("El número de reprobados es de: ")
print(reprobados)