import os
print("Bienvenido a mi segundo programa python!")
print("Esto conciste en que tu me darás un número, y yo te imprimiré la lista de los anteriores al mismo, ¿Listo?")
num=int(input("Dame un número"))
for i in range(-0,num):
    print(i, ", ")
print("Ahora vamos de regreso!")
os.system("pause")