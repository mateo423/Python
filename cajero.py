# este es una forma de hacer lo pero como tal  solo podemos retirar dinero del banco 
saldo_inicia = 1000
print("/t:Menu:")
print("1. Ingresa dinero ala cuenta")
print("2. retirar dinero de la cuenta")
print("3. Mostrar el dinero disponible")
print("4. Salir")

opcion = input("Ingrese una opcion: ")
if opcion == "1":
        dinero = float(input("Cuato dinero deseas ingresar: "))
        saldo_inicia += dinero
        print(f"El saldo Actual es: {saldo_inicia}")

elif opcion =="2":
        retirar = float(input("Cuanto dinero deseas retirar :"))
        saldo_inicia -= retirar 
        print(f'su saldo es: {saldo_inicia} ')

        if retirar > saldo_inicia:
            print("No puedes sacar ese dinero")

elif opcion =="3":
        print(f"El saldo Actual es: {saldo_inicia}")

elif opcion =='4':
        
    print("Adios")



else:
            saldo_inicia = saldo_inicia - retirar
print("Error no sabes leer jil de mierda hay solamente 1 opcion gey")
