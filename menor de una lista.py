list=[]
for x in range(5):
    v=int(input("Dame valor: "))
    list.append(v)
menor=list[0]
lugar=0
for x in range(1,5):
    if list[x]<menor:
        menor=list[x]
        lugar=x
print("La lista completa es: ", list)
print("El menor es: ", menor)
print("El lugar del menor es: ", lugar)