cal1=int(input("Dame la calificación 1"))
cal2=int(input("Dame la calificación 2"))
cal3=int(input("Dame la calificación3"))
promedio=cal1+cal2+cal3/3
if promedio>=7:
    print("Aprobado!")
else:
    if promedio<=6:
        print("Te falta mejorar, bien")
    else:
        print("Reprobado!")