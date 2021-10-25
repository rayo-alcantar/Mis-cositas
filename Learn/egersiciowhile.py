import random

value = random.randint(1, 5)
count = 0
guess = 0
while guess != value:
    count += 1
    guess = input('Adivina un número entre 1 y 5: ')
    if guess.isnumeric():
        guess = int(guess)
else:
    print(f'Lo adivinaste en {count} intentos!')