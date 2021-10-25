list1=[]
list2=[]

for i in range(8):
    pregunta=(input("Mañana o Tarde?"))
    if pregunta=="Mañana":
        m=int(input("Dame sueldo: "))
        list1.append(m)
    else:
        if pregunta=="Tarde":
            t=int(input("Dame sueldo: "))
            list2.append(t)
print("Los sueldos de la  mañana son: ")
print(list1)
print("Los sueldos de la tarde son: ")
print(list2)