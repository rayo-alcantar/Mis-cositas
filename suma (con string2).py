"""Programa que pide  uno o más valores por teclado, mientras pregunta al usuario  si quiere  seguir añadiendo mas números con un operador, y al finál entregar resultado de suma"""
pregunta="sí"
suma=0
while pregunta=="sí":
    v=int(input("Dame número: "))
    suma=suma+v
    pregunta=(input("Quieres agregar otro número? sí/no"))
print("La suma es: ", suma)