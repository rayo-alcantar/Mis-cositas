#Validar que una clabe sea mayor a 10, pero inferior a 20.
x=0
contador=0
print("Deverás  ingresár una contraseña (Mayor a 10 ymenor de 20 caracteres)")
password=(input("Ingresa tu contraseña: "))
while x<len(password):
    contador=contador+1
    x=x+1
if contador>10 and contador<21:
    print("Contraseña válida!")
else:
    if contador<10:
        print("Contraseña menor!")
    else:
        if contador>20:
            print("Contraseña mayor!")