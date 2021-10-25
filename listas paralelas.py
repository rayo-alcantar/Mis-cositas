nombres=[]
edades=[]
for x in range(5):
    n=(input("Dame el nombre de la persona: "))
    nombres.append(n)
    e=int(input("Dijita la edad de la persona: "))
    edades.append(e)
print("Nombre de las personas mayores de  edad: ")
for x in range(5):
    if edades[x]>=18:
        print(nombres[x])
