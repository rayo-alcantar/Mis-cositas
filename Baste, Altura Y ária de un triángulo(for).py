superficie=0
superficiem=0
n=int(input("Cuantos triángulos serán?"))
for x in  range(n):
    base=int(input("Dame la base"))
    altura=int(input("Dame la altura"))
    a=base*altura//2
    if a>=12:
        superficiem=superficiem+1
    print("La base es: ", base)
    print("La altura es: ", altura)
    print("El ária es: ", a)
print("Y el  número de árias  mayores a 12 son: ", superficiem)