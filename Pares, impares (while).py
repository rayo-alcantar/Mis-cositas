x=1
pares=0
impares=0
n=int(input("Cuantos números serán?"))
while x<=n:
    c=int(input("Dame número..."))
    if c%2==0:
        pares=pares+1
    else:
        impares=impares+1
    x=x+1
print("El totál de números pares son de: ")
print(pares)
print("El total de números impares es de: ")
print(impares)