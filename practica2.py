import math

print()
print("Bienvenidos a este programa XD")
print()
print()


def name(nombre):
    print(f' hola {nombre} encantando de saludarte')


name(nombre=input("como te llama : "))

opciones = int(input("Hola bienvenido a este programa  donde tu puedes realizar varios varios programa bueno aqui \n"
                     "veras una  lista de que programa puedes realizar \n 1-Calculadora \n 2-Programade edades \n "
                     "3-sacar un numero par y impar \n"
                     "cual de estas operaciones deseas realizar -> "))
if opciones == 1:
    num1 = int(input("ingrese el numero a -> "))
    num2 = int(input("ingrese el numero b -> "))
    menu = int(input(
        """Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-Salir \n 6-elevacion \n 
        7-raiz \n ->  cual de las operaciones quieres relaizar escribe el numero -> """))

    if menu == 1:
        suma = num1 + num2
        print(f"El resultado de su suma es: {suma}")
        menu = int(input("""Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-Salir \n 
        6-elevacion 7-raiz \n ->  cual de las operaciones quieres relaizar escribe el numero -> """))

    if menu == 2:
        resta = num1 - num2
        print(f"El resultado de su resta es : {resta}")
        menu = int(input(
            """Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-Salir \n 6-elevacion \n 
            7-raiz \n ->  cual de las operaciones quieres relaizar escribe el numero -> """))
    if menu == 3:
        multiplicaion = num1 * num2
        print(f"El resultado de su multiplicaion es {multiplicaion}")
        menu = int(input(
            """Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-Salir \n 6-elevacion \n 
            7-raiz \n ->  cual de las operaciones quieres relaizar escribe el numero -> """))
    if menu == 4:
        division = num1 / num2
        print(f"El resultado de su division es : {division}")
        menu = int(input(
            """Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-Salir \n 6-elevacion \n 
            7-raiz \n ->  cual de las operaciones quieres relaizar escribe el numero -> """))

    if menu == 6:
        elevacion = num1 ** num2
        print(f"El resultado de  la elevacion  es {elevacion}")
        menu = int(input(
            """Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-Salir \n 6-elevacion \n 
            7-raiz \n->  cual de las operaciones quieres relaizar escribe el numero -> """))

    if menu == 7:
        num1 = float(input("Ingrese el numero que desea sacar de una raiz : "))
        raiz = math.sqrt(num1)
        print(f"el resultado de su raiz es {raiz}")
        menu = int(input(
            """Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-Salir \n 6-elevacion \n 
            7-raiz \n   cual de las operaciones quieres relaizar escribe el numero -> """))
    elif menu == 5:
        print("Gracias por participar")


if opciones == 2:
    edad = int(input('digite su edad -> '))

    if 0 < edad < 100 and edad > 18:
        print("eres mayor de edad")

    elif 0 < edad < 18:
        print('eres menor de edad')

    elif edad == 18:
        print("eres mayor de edad ")

    elif edad > 100:
        print("usted no puede tener esa edad en la tierra")
    else:
        print("su edad es incorrecta")

if opciones == 3:
    num1 = int(input("Digite su primer numero : "))
    num2 = float(input("Digite su segundo numero : "))
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("ambos numeros son par")
    elif num1 % 2 == 0 and num2 % 2 != 0:
        print("El primer numero es par")
        print(num1, 'es par')
    elif num1 % 2 != 0 and num2 % 2 == 0:
        print("El segundo numero es par")
        print(num2, 'es par')
    else:
        print("ERROR")
