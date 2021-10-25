alumno=[]
calificacion=[]
contador=0
for x in range(4):
    a=(input("Nombre del alumno: "))
    alumno.append(a)
    c=float(input(" calificación: "))
    calificacion.append(c)
for x in range(4):
    if calificacion[x]>=8:
        print(alumno[x])
        print(calificacion[x])
        print("Muy Bueno!")
        contador=contador+1
    else:
        if calificacion[x]>4 and calificacion[x]<8:
            print(alumno[x])
            print(calificacion[x])
            print("Regular.")
        else:
            if calificacion[x]<4:
                print(alumno[x])
                print(calificacion[x])
                print("Insuficiente.")
print("El número de alumnos con la nota: Muy bueno!  es de: ", contador)