x=1
total=0
ct=0
mt=0
n=int(input("Cuantos empleados son?"))
while x<=n:
    s=int(input("Cuanto  ganas?"))
    total=total+s
    if s>=100 and s<=300:
        ct=ct+1
    else:
        if s<100:
            print("Error!")
        if s<=500:
            mt=mt+1
    x=x+1
print("El total de la empresa por todo es de: ")
print(total)
print("Los empleados que ganan entre 100 y 300 son: ")
print(ct)
print("Los que ganan más de 300 son de: ")
print(mt)