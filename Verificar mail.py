"""Programa que pida un mail, y  verifique que solo tenga un @"""
print("Verifiquemos que su  mail sea una dirección  válida")
x=0
contador=0
mail=(input("Ingrese su mail: "))

while x<len(mail):
    if mail[x]=="@":
        contador=contador+1
    x=x+1
if contador==1:
    print("Bien, tu mail es una dirección  válida")
else:
    print("Disculpa, tu mail no es válido!")