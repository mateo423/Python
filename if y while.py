#Hoy veremos ejemplos  del if y del while unidos XD

#Programa  para pedir un numero psotivo

#le indicamos que si while es verdadero
while True:
    numero = int(input("ingreese su numero positivo: -> "))
  # Creamos una condicion que si numero es menor a 0 es falsoxd
    if numero < 0: 
        print("le dije que el numero debe ser positivo")
        # despues usamos el else que es lo contrario del if
        # y creamos una variable para continuar con la operacion
    else:
        print("ha escrito el numero -> ", numero)
    r = input(f"desea continua? -> ")
    # aca creamos una condicion que la variable r es igual a si
    #con esto le estamos indicando contatenadno para seguir con las operaciones 
    # para que el programa no termine
    if r == "si":
        numeros = int(input("ingrese su numero positivo:"))
        if numeros < 0: 
            print("le dije que el numero debe ser positivo")
        else:
            print("ha escrito el numero:", numeros)
            r = input(f"desea continua?")
            # el break es para parar osea para que no mas se repita 
        break

#Programa para ingresar resultado de suma y resta 

#1. creamos variable que tendran almanenado un int y una input

a = int(input("ingrese el numero a>"))
b = int(input("ingrese el numero b>"))
# aca creamos una variable llamada menu que va hacer nuestro menu de operaciones xd
menu = int(input('Menu pincipal: /n 1-suma /n 2-resta /n 3-multiplicacion /n 4-division /n 5-salir /n ->  cual de las operaciones quieres relaizar escribe el numero -> '))
# le estamos indicando al while que es diferente a 0 ya que  no tenemos operaciones  en 0 xd
while menu != 0:
    #creamos la condicion que la opcion del menu es igual a el numero 1 
    if menu== 1 :
        #despues le metemos la operacion que va a encargada la opcion 
        c = a+b
        # y imprimimos la  suma 
        print("el resultado de la suma es >", c)
        # xd aca hacemos el mismo proceso  no ce como hacerlo para que se repita las operaciones pero bueno xd
        menu = int(input('Menu pincipal: /n 1-suma /n 2-resta /n 3-multiplicacion /n 4-division /n 5-salir /n'))
        # aca creamos el elif  que if si no se cumple if se cumple elif pero si no se cumple elif se cumple else
    elif menu== 2 :
        c = a-b
        print("el resultado de la resta es >", c)
        menu = int(input('Menu pincipal: /n 1-suma /n 2-resta /n 3-multiplicacion /n 4-division /n 5-salir /n'))
    elif menu == 3:
         c = a*b
         print("el resultado de la multiplicacion es >", c)
         menu = int(input('Menu pincipal: /n 1-suma /n 2-resta /n 3-multiplicacion /n 4-division /n 5-salir /n'))
    elif menu == 4 :
         c = a/b
         print("el resultado de la division es >", c)
         menu = int(input('Menu pincipal: /n 1-suma /n 2-resta /n 3-multiplicacion /n 4-division /n 5-salir /n'))
    else:
         print("Error no seas idiota aprende a leer te estamos dando indicaciones solo seguilas")
         break