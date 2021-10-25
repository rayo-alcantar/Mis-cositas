n1=int(input("Dame número 1"))
n2=int(input("Dame número 2"))
n3=int(input("Dame número 3"))
print("El número más grande es... ")
if n1>n2 and n1>n3:
    print(n1)
else:
    if n2>n3:
        print(n2)
    else:
        print(n3)