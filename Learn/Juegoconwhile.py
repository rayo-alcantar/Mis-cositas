import random
v = 0
c = 0
n = 0
l = 0
L = int(input('Cual será el límite del random?'))
v = random.randint(1, l)
while n != v:
    c= c +1
    if n < v:
        print('Es más grande!')
    else:
        if n > v:
            print('Es más chico!')
print(f'Lo adivinaste en {c} intentos!')