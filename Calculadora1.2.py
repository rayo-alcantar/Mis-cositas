from tkinter import*

if __name__ == "__main__":
    ventana = Tk()
    ventana.configure(background="light blue, ")
    ventana.geometry("265x125")
    ventana.mainloop()
    
    ventana.title("Calculadora de Ángel  V1.0")
    calculo = StringVar()
    datos = Entry(ventana, textvariable=calculo)
    datos.grid(columnspan=10, ipadx=50)
    boton1 = Button(ventana, text=' 1 ', fg='black', bg='white',
    command=lambda: digito(1), height=1, width=7)
    boton1 = Button(ventana, text=' 1 ', fg='black', bg='white',
    command=lambda: digito(1), height=2, width=5)
    boton1.grid(row=2, column=0)
    boton2 = Button(ventana, text=' 2 ', fg='black', bg='white',
    command=lambda: digito(2), height=2, width=5)
    boton2.grid(row=2, column=1)
    boton3 = Button(ventana, text=' 3 ', fg='black', bg='white',
    command=lambda: digito(3), height=2, width=5)
    boton3.grid(row=2, column=2)
    boton4 = Button(ventana, text=' 4 ', fg='black', bg='white',
    command=lambda: digito(4), height=2, width=5)
    boton4.grid(row=3, column=0)
    boton5 = Button(ventana, text=' 5 ', fg='black', bg='white',
    command=lambda: digito(5), height=2, width=5)
    boton5.grid(row=3, column=1)
    boton6 = Button(ventana, text=' 6 ', fg='black', bg='white',
    command=lambda: digito(6), height=2, width=5)
    boton6.grid(row=3, column=2)
    boton7 = Button(ventana, text=' 7 ', fg='black', bg='white',
    command=lambda: digito(7), height=2, width=5)
    boton7.grid(row=4, column=0)
    boton8 = Button(ventana, text=' 8 ', fg='black', bg='white',
    command=lambda: digito(8), height=2, width=5)
    boton8.grid(row=4, column=1)
    boton9 = Button(ventana, text=' 9 ', fg='black', bg='white',
    command=lambda: digito(9), height=2, width=5)
    boton9.grid(row=4, column=2)
    boton0 = Button(ventana, text=' 0 ', fg='black', bg='white',
    command=lambda: digito(0), height=2, width=5)
    boton0.grid(row=5, column=0)
    suma = Button(ventana, text=' + ', fg='black', bg='white',
    command=lambda: digito("+"), height=2, width=5)
    suma.grid(row=2, column=3)
    resta = Button(ventana, text=' - ', fg='black', bg='white',
    command=lambda: digito("-"), height=2, width=5)
    resta.grid(row=3, column=3)
    multiplica = Button(ventana, text=' * ', fg='black', bg='white',
    command=lambda: digito("*"), height=2, width=5)
    multiplica.grid(row=4, column=3)
    divide = Button(ventana, text=' / ', fg='black', bg='white',
    command=lambda: digito("/"), height=2, width=5)
    divide.grid(row=5, column=3)
    resultado = Button(ventana, text=' = ', fg='black', bg='white',
    command=igual, height=2, width=5)
    resultado.grid(row=5, column=2)
    limpiar = Button(ventana, text='Limpiar', fg='black', bg='white',
    command=limpiar, height=2, width=5)
    limpiar.grid(row=5, column='1')
def digito(num):
    global boton
    boton = boton + str(num)
    calculo.set(boton)
def igual():
    tratar:
        global boton
        total = str(eval(boton))
        calculo.set(total)
        boton = ""
    excepto:
        calculo.set(" error ")
def limpiar:
    calculo.set("")
    