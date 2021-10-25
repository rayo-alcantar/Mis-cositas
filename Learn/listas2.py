import random
numeros= []
while len(numeros) < 5:
    numeros.append(random.randint(1, 100))
for n in numeros:
    print(n)
    if n >= 90:
        print('Encontrado un número mayor a 90.')
        break
else:
    print('No hay números mayores a 90')
    print('Completado!')