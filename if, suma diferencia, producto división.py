for i in range(10):
 numero=int(input("Escribe un número"))
 numeros=numero
 contadorc=0
 contadorb=0
if numeros%3==0:
 contadorc=contadorc+1
else:
 if numeros%5==0:
  contadorb=contadorb+1

 print("Hay: ", contadorc, ", números múltiples de 3. Y hay: ", contadorb, ", números de múltiple 5.")
