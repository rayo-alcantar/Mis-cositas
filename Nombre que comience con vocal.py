#Programa que  pide el nombre del usuario, e indica si comienza con vocál.
print("Me darás un nombre (por favor que comience con mayúscula) y yo te diré si comienza con bocál")
nombre=(input("Dame el nombre: "))
if nombre[0]=="A" or nombre[0]=="E" or nombre[0]=="I" or nombre[0]=="O" or nombre[0]=="U":
    print("Tu nombrre comienza con vocal, y es la ", nombre[0])
else:
    print("Tu nombre no comienza con vocal.")