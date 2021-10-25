usuarios=[]
for x in range(3):
    u=(input(" Quien se unió a la mesa?"))
    usuarios.append(u)
print("3 Personas están sentadas en la mesa: ")
print(usuarios[0], ", ", usuarios[1], " y ", usuarios[2])
print("El jefe de mesa es ", usuarios[0])
n=int(input("Elija el nuevo jefe de mesa: Con el número en el que el usuario esté listado: "))
if n==2:
    aux=usuarios[0]
    usuarios[0]=usuarios[1]
    usuarios[1]=aux
else:
    if n==3:
        aux=usuarios[0]
        usuarios[0]=usuarios[2]
        usuarios[2]=aux
print("3 personas están sentadas en la mesa: ")
print(usuarios[0], ", ", usuarios[1], " y ", usuarios[2])
print("El jefe de mesa es ", usuarios[0])