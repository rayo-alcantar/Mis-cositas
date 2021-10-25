contador=0
promedio=0
x=0
while x<=10:
 numero=int(input("Escribe un número."))
 contador=contador+numero
 x=x+1

 promedio=contador/10
print("Este es el resultado de la suma de los números ingresados: ", contador, ", y este es el promedio de la suma: ", promedio)
