fa=input('Dame los grados fahrenheit a convertir a celsius: ')
if fa.isnumeric()==False:
    print("Solo números!")
    exit()

ce=int((fa - 32) * 5/9)
print(fa, ' grados fahrenheit es igual a ', ce, ' grados celsius!')