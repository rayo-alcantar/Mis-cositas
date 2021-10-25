"""Programa que te pedirá los  nombres de 2 personas, para luego pedir una contraseña.
Después simulará un login."""
print("Te pediré los datos de login de 2 personas diferentes.")
print("Registro de la persona 1.")
name1=(input("Cual es tu nombre, persona uno?"))
password1=(input("Cual es tu contraseña, persona uno?"))
print("Registro de la persona 2")
name2=(input("Cual es tu nombre, persona dos?"))
password2=(input("Cual es tu contraseña, persona dos?"))
n=int(input("Cuantas veces quieres tratar de iniciar seción?"))
for x in  range(1, n, 1):
    login=(input("Quien eres?"))
    if login==name1:
        print("Comprueva que eres: ", name1)
        past=(input("Escribe tu contraseña."))
        if past==password1:
            print("Bienvenido ", name1, "!")
        else:
            print("No eres ", name1, "!")
    else:
        if login==name2:
            print("Prueba que eres ", name2)
            past=(input("Escribe tu contraseña."))
            if past== password2:
                print("Bienvenido ", name2, "!")
            else:
                print("No eres ", name2, "!")
    