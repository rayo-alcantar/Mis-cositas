nombreusuario=(input("Escribe tu nombre con el que iniciarás sesión."))
contraseusuario=(input("Escribe la contraseña con la que iniciarás sesión."))
numeroveces=int(input("Escribe la cantidad de veces con la que deseas iniciar sesión"))
for iniciar in range(numeroveces):
  nombre=(input("Escribe el nombre de usuario con el que te registraste."))
  contrase=(input("Escribe la contraseña con la que te registraste."))
  if nombre==nombreusuario and contrase==contraseusuario:
   print("¡Bienvenido!")
  else:
   print("Tu nombre de usuario o contraseña no existen.")
   if nombre==nombreusuario:
    print("")
   else:
    print("No, ese nombre de usuario no es válido.")
