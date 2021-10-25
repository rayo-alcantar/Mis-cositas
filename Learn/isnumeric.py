n1 = input('Número 1: ')
n2 = input("Número 2: ")
if n1.isnumeric() == False or n2.isnumeric() == False:
    print("Solo números, puta madre!")
    exit()
n1 = int(n1)
n2 = int(n2)
sum = n1 + n2
print("Suma: " + str(sum))