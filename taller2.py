#Programa  para pedir un numero psotivo
while True:
    numero = int(input("ingreese su numero positivo:"))
    if numero < 0: 
        print("le dije que el numero debe ser positivo")
    else:
        print("ha escrito el numero:", numero)
    r = input(f"desea continua")
    if r == "si":
        numeros = int(input("ingreese su numero positivo:"))
        if numeros < 0: 
            print("le dije que el numero debe ser positivo")
        else:
            print("ha escrito el numero:", numeros)
            r = input(f"desea continua")
        break