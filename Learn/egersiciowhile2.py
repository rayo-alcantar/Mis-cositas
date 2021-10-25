import random
#Se declara la variable que contendrá el número a adivinar
v = 0
# Se declara la variable que contará para el while
c = 0
# Se declara la variable para el usuario
n = 0
# Se le da el valor random a la variable
v = random.randint(1,5)
# Si la variable contar, es diferente a la variable del valor, el while se ejecutará
while c != v:
    # Se declara la entrada de texto para el usuario.
    n = int(input('Adivina el número entre 1 y 5!'))
    # Se evalúa si la variable n es menor a la variable v
    if n < v:
        print('Es más grande!')
    else:
        if n > v:
            print("Es más chico!")
    c = c +1
print(f'Lo lograste en {c} intentos!')§