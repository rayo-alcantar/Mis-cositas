p=int(input("¿Cuantas preguntas fueron en totál?"))
c=int(input("¡Cuantas se respondieron  correctamente?"))
porcentaje=c/p*100
if porcentaje>=90:
    print("Genial! Estás en el nivel máximo!")
else:
    if  porcentaje>75:
        print("Nivel medio, no está mal. Pero podría ser mejor.")
    else:
        print("No pasas!")