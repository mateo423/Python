
#Programa para ingresar resultado de suma y resta 
a = int(input("ingrese el numero a>"))
b = int(input("ingrese el numero b>"))
menu = int(input('Menu pincipal: /n 1-suma /n 2-resta /n 3-multiplicacion /n 4-division /n 5-salir /n'))
while menu != 0:
    if menu== 1 :
        c = a+b
        print("el resultado de la suma es >", c)
        menu = int(input('Menu pincipal: /n 1-suma /n 2-resta /n 3-multiplicacion /n 4-division /n 5-salir /n'))
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
         print("elige una opcion")
         break