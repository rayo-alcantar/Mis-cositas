list1=[]
list2=[]
list3=[]
suma=0
for x in range(5):
    l1=int(input("Dame los díjitos de la primera lista: "))
    list1.append(l1)
    l2=int(input("Dame díjitos de la lista 2: "))
    list2.append(l2)
for x in range(5):
   suma=list1[x]+list2[x]
   list3.append(suma)
print("La suma de ambas listas es: ")
print(list3)