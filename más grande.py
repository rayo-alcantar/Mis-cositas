n1=int(input("Dame el número 1"))
n2=int(input("Dame número 2"))
n3=int(input("Dame número 3"))
if n1>n2:
    if n1>n3:
        print("El número 1 es el más grande!")
    if n3>n2:
        print("El número 3 es el más grande!")
else:
    print("El número 2 es el más grande!")