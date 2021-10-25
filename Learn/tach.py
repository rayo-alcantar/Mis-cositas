repite = True
number1 = input("elija un número por favor: ")
while repite == True:
    try:
        number1 =int(number1)
        repite =     False
    except:
        number1 = input("no has escogido un número, escoge un número por favor: ")

number1 =int(number1)
number2 = input("elige el segundo número: ")
try:
    number2 = int(number2)
except:
    number2 = input("no has elegido un número, elige uno por favor")
    number2 =int(number2)
print ("ya que has elegido los dos números principales, vamos a jugar un poco:")
print ("ya tenemos los dos números, tú decidirás qué operación podemos hacer con ellos: ")
print ("si presionas el número 1, los dos números anteriormente elegidos se sumarán. Si eliges el 2, ambos números se restarán:")
print ("si eliges el 3, los números se multiplicarán y si eliges el 4, los números se dividirán:")
choose = input("¿cuál número elegirás?: ")
if choose == "1":
    print ("el resultado de su suma es:", number1 +number2)
elif choose == "2":
    print ("el resultado de tu resta es: ", number1 -number2)
elif choose == "3":
    print ("el resultado de tu multiplicación es: ", number1 *number2)
elif choose == "4":
    print ("el resultado de tu dibisión es: ", number1 /number2)
else:
    print ("no has elegido una opción válida: por favor elige una.")