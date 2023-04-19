# hacer un programa donde la edad de 18 es mayor de edad y menor de edad

edad = int(input('digite su edad'))

if edad > 0 and edad > 18 and edad <100:
    print("eres mayor de edad")
elif edad > 0 and edad < 18:
    print('eres menor de edad')
elif edad == 18:
    print("eres mayor de edad 18")
elif edad > 100 :
    print("usted no puede tener esa edad en la tierra")
else :
    print("su edad es incorrecta")


#Hacer que pida un caracter e indiquue si es una vocal o no

letra = input('Digite su caracter')
letra = letra.lower()

if letra=='a' or letra=='e' or letra =='i' or letra== 'o' or letra=='u':
    print('el caracter que ha colocado es una vocal')
else :
    print('esto no es una vocal sapa')


#hacer una calculadora que haga operaciones arigmeticas

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
elif c == 'r' :
    print(f'el resultado es la resta de los numeros es : {resta}')
elif c == 'm':
    print(f'el resultado es la multiplicacion de los numeros es :{multiplicacion}')
elif c == 'd' :
    print(f'el resultado es la division de los numeros es :{division}')
else:
    print("su operacoin esta erronea asegurate de poner las variables bien")