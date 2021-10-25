pregunta="si"
suma=0
while pregunta=="si":
    v=int(input("Dame un número: "))
    suma=suma+v
    pregunta=(input("Quieres agregar otro número? si/no"))
print("La suma es: ", suma)