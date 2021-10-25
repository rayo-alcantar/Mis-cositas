#Programa  que valida cuantas vocales hay en la oración.
print("Dame una oración, con mayúsculas, y al finál te diré cuantas vocales ingresaste.")
contador=0
x=0
oracion=(input("Comienza a escribir!"))
o=oracion.lower()
while x<len(o):
    if o[x]=="a" or o[x]=="e" or o[x]=="o" or o[x]=="i" or o[x]=="u":
        contador=contador+1
    x=x+1
print("En totál ingresaste ", contador, " vocales.")