n1=int(input("Dame el primer número, de 3."))
n2=int(input("Dame el segundo número"))
n3=int(input("Dame el último número."))
if n1>n2 and n1>n3:
    print("El número más grande, es:")
    print(n1)
    if n2>n3:
        print("El número más pequeño  es: ")
        print(n3)
    else:
        print("El número más pequeño es: ")
        print(n2)
else:
    if n2>n3:
        print("El número más grande es: ")
        print(n2)
    else:
        if n3>n1:
            print("El número más pequeño es: ")
            print(n1)
        else:
            print("El número más chico es: ")
            print(n3)