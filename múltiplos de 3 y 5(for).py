num3=0
num5=0
for x in range(10):
    n=int(input("Dame un número"))
    if n%3==0:
        num3=num3+1
    else:
        if n%5==0:
            num5=num5+1
print("Números que son  múltiplos de 3")
print(num3)
print("Números que son múltiplos de 5")
print(num5)