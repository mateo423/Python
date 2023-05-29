try:
    numero =int(input('Ingrese un numero entero : '))
    print(f'su numero entero que ingreso es : {numero}')
except ValueError:
    print("Error al ingresar el numero, el numero debe de ser entero")
