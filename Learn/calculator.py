print("Bienvenido a mi calculadora simple!")
n1=int(input('Primer número? '))
o=input('Operación a realizar? (+) suma, (-) resta, (*) multiplicación, (/) división, (%) residuo y (**) exponente.')
if o=="":
    print('¡Ingresa una operación válida!')
    exit()
elif  o=='+':
    n2=int(input('Dame segundo númnero: '))
    sum=n1+n2
    print('La suma es: ', sum)
else:
    if o=='-':
        n2=int(input('Segundo número: '))
        rest=n1-n2
        print('La resta es: ', rest)
if o=='*':
    n2=int(input('Segundo número: '))
    mult=n1*n2
    print('~La multiplicación es: ', mult)
elif o=='/':
    n2=int(input('Segundo número: '))
    div=n1/n2
    print('La división es: ', div)
else:
    if o=='%':
        n2=int(input('Segundo número: '))
        res=n1%n2
        print('El residuo es: ', res)
if o=='**':
    n2=int(input('Segundo número: '))
    exp=n1**n2
    print('El exponente es: ', exp)