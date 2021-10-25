for i  in range(5):
    cal=int(input("Dime tu calificación."))
    if cal>=6 and cal<=10:
        print("Bien, pasaste.")
    else:
        if cal>=1 and cal<=5:
            print("no, reprobaste.")
        if cal<=0:
            print("en esta institución, no calificamos con esa nota.")
        if cal>=11:
            print("No existe, no existe.")
            