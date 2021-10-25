import random
numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
elegir = random.choice(numbers)
print(elegir)
elegir = random.choices(numbers, k = 3)
print(elegir)
