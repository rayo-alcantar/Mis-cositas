#Programa que cuenta los espacios en blanco de una oración
x=0
contador=0
oracion=(input("Escribe una oración..."))
while x<len(oracion):
    if oracion[x]==" ":
        contador=contador+1
    x=x+1
print("En total ingresaste ", contador, "De Espacios.")