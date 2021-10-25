n=int(input("Dame el número (Máximo 3 cifras)"))
if n>9:
    if n<100:
        print("El número es de 2 cifras")
    else:
        if n<1000:
            print("El número es de 3 cifras")
        else:
            print("Error! Dije 3 Cifras máximo!")
else:
    print("El número es de una cifra")