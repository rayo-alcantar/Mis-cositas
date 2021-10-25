"""Programa que  pide nombre, luego te pide el número de carácter  del  nombre que  quieres que el programa te devuelva"""
print("Me darás un nombre, para después darme el número del carácter del nombre que quieres que te muestre.")
nombre=(input("Cual es la  cadena de texto?"))
v=int(input("Qué número de carácter quieres que te devuelva?"))
print(nombre[v])
print("Tu cadena tiene ", len(nombre), " letras")