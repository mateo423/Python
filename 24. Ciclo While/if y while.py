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
    if r == "no":
        break
    if r == "si":
        numeros = int(input("ingrese su numero positivo:"))
        if numeros < 0: 
            print("le dije que el numero debe ser positivo")
        else:
            print("ha escrito el numero:", numeros)
            r = input(f"desea continua?")
            # el break es para parar osea para que no mas se repita 
        break
