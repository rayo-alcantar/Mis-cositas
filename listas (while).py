x=1
x2=1
suma1=0
suma2=0
lista1=0
lista2=0

while x<=15:
    lista1=int(input("Dame díjito"))
    suma1=suma1+lista1
    x=x+1
while x2<=15:
    lista2=int(input("Dame díjito de la lista 2"))
    suma2=suma2+lista2
    x2=x2+1
if suma1>suma2:
    print("La lista más grande es: ")
    print("Lista 1!", suma1)
else:
    if suma2>suma1:
        print("La lísta más grande es: ")
        print("La 2!", suma2)
    else:
        print("Son iguales")