#Preguntar la identidad.
per1=(input("Hola, ¿Como te llamas?"))
pass1=(input("¿Cuál será tu contraseña?"))
#Registro 2.
per2=(input("¿Hola, ¿Como te llamas?"))
pass2=(input("¿Cuál será tu contraseña?"))
n=int(input("¿Cuantos intentos quieres?"))
for i in range(n):
    name1=(input("¿Quién eres?")
    if name1==per1:
        passw=int(input("Dame tu contraseña: "))
        if passw==pass1:
            print("Bienvenido, ", per1, "!")
        else:
            print("Contraseña incorrecta, inténtalo otra vez.")
        