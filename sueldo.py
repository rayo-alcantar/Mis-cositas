at=int(input("¿Cuantos años llebas trabajando?"))
s=int(input("¿Cual es tu sueldo por año?"))
if at>=10 and s<500:
    sueldo=20/100*s
    print("Tendrás un aumento del 20%,  tu sueldo finál será de: ")
    print(sueldo)
else:
    if at<10 and s>=500:
        sueldo=5/100*s
        print("Tu aumento será del 5%, y tu sueldo actual será de: ")
        print(sueldo)
    else:
        if s>=500:
            print("Tu sueldo no cambia, seguirá siendo: ")
            print(s)