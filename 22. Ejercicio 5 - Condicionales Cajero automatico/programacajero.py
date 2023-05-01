''' Hacer un programa que simule un cajero automatico con 
saldo inicial de 1000 y tendra el siguente menu de opciones :

1. Ingresar dinero
2. Sacar dinero
3. Ver saldo
4. Salir
'''

# Otra manera de hacerlo 
saldo = 1000
print("/t:Menu:")
print("1. Ingresa dinero ala cuenta")
print("2. retirar dinero de la cuenta")
print("3. Mostrar el dinero disponible")
print("4. Salir")
opcion = input("Ingrese una opcion: ")

print()

if opcion == "1":
    extras = float(input('Cuanto dinero deseas ingresar: '))
    saldo += extras
    dinero = input(f"su dinero total es :{saldo}")
elif opcion =='2':
    retirar = float(input('Cuanto dinero deseas retirar: '))
    saldo -= retirar
    dinero = input(f"su dinero total es {saldo}:")
elif opcion =="3":
    dinero = input(f"Su saldo  es :{saldo} ")

elif opcion =="4":
    print("Adios")
else:
    print("No es una opcion valida")








