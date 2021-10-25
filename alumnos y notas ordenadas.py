alumnos=[]
notas=[]
for x in range(5):
    n=(input("Ingrese nombre: "))
    alumnos.append(n)
    cal=int(input("Ingrese nota del alumno en cuestión: "))
    notas.append(cal)
for k in range(4):
    for x in range(4):
        if notas[x]<notas[x+1]:
            aux1=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux1
            aux2=alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x+1]=aux2
print("Lista de alumnos con calificación ordenada de  mayor a menor: ")
for x in range(5):
    print(alumnos[x], notas[x])