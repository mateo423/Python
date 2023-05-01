# hacer una calculadora que haga operaciones arigmeticas

a = float(input('ingrese un numero: '))
b = float(input('ingrese otro numero: '))
c = input("""ingrese la operacion:
s = suma
r = resta
m = multiplicacion
d = division 
 cual de las siguentes operaciones desea hacer : """)

suma = a+b
resta = a-b
multiplicacion = a*b
division = a/b

if c == 's':
    print(f'el resultado es la suma de los numeros es : {suma}')
elif c == 'r':
    print(f'el resultado es la resta de los numeros es : {resta}')
elif c == 'm':
    print(f'el resultado es la multiplicacion de los numeros es :{multiplicacion}')
elif c == 'd':
    print(f'el resultado es la division de los numeros es :{division}')
else:
    print("su operacoin esta erronea asegurate de poner las variables bien")
