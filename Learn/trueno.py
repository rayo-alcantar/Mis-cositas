x = 0
version='1.1'
print('Bienvenido al insultador de truenos, versión ', version, '!')
print("Deberás escribir trueno de diferentes maneras y en base a eso, insultaré diferente! Podrás descubirr todos los insultos?")
v = int(input("Cuantos intentos quieres?"))
while x <= v:
    x = x+1
    t = input('Dame tu trueno: ')
    if t=='':
        print('Solo truenos válidos!')

    elif t.isnumeric()== True:
        print("Solo cadenas de texto!")
    else:
        if t=='trueno':
            print('Trueno cabrón!')
        elif t=='Trueno':
            print('Trueno puto!')
        elif t == "TrUenO":
            print("Trueno, me cago en tu puta desendencia!")
        elif t == "TRueno":
            print("Como chingas, trueno!")
        elif t == "trueNO":
            print("Hijo de tu puta madre, trueno!")
        elif t == "truEnO":
            print("Vete a la puta qe te reparióooo!")
        elif t == "TRUeno":
            print("Filo do puta!")
        elif t == "truENO":
            print("filho da mãe!")
        elif t == "trueeno":
            print("Hurensohn!")
        elif t == "truenO":
            print("Hijo eputa")

        else:
            if t=='TRUENO':
                print('Trueno, la concha de tu madre!')