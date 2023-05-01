
#Programa para ingresar resultado de suma y resta 

#1. creamos variable que tendran almanenado un int y una input

a = int(input("ingrese el numero a -> "))
b = int(input("ingrese el numero b -> "))
# aca creamos una variable llamada menu que va hacer nuestro menu de operaciones xd
menu = int(input('Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-salir \n ->  cual de las operaciones quieres relaizar escribe el numero -> '))
# le estamos indicando al while que es diferente a 0 ya que  no tenemos operaciones  en 0 xd
while menu != 0:
    #creamos la condicion que la opcion del menu es igual a el numero 1 
    if menu== 1 :
        #despues le metemos la operacion que va a encargada la opcion 
        c = a+b
        # y imprimimos la  suma 
        print("el resultado de la suma es >", c)
        # xd aca hacemos el mismo proceso  no ce como hacerlo para que se repita las operaciones pero bueno xd
        menu = int(input('Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-salir \n'))
        # aca creamos el elif  que if si no se cumple if se cumple elif pero si no se cumple elif se cumple else
    elif menu== 2 :
        c = a-b
        print("el resultado de la resta es >", c)
        menu = int(input('Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-salir \n'))
    elif menu == 3:
         c = a*b
         print("el resultado de la multiplicacion es >", c)
         menu = int(input('Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-salir \n'))
    elif menu == 4 :
         c = a/b
         print("el resultado de la division es >", c)
         menu = int(input('Menu pincipal: \n 1-suma \n 2-resta \n 3-multiplicacion \n 4-division \n 5-salir \n'))
    elif menu == 5:
        print("Ok, Gracias por participar")
        break
    else:
         print("Error no seas idiota aprende a leer te estamos dando indicaciones solo seguilas")
         break