import random

roll = 0
contar = 0
print("¡La primera persona en sacar un 5 gana!")
while roll != 5:
    name = input("Ingrese un nombre, o q para salir: ")
    if name.strip() == '':
        continue
    if name == 'q':
        break
    contar = contar +1
    roll = random.randint(1,5)
    print(f"{name} arrojó {roll}")
else:
    print(f"{name} gana!")
print(f"Has tirado el dado {contar} veces.")