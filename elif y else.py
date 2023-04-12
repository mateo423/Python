#programa donde el usuario debe ingresar un numero positivo 
numero = int(input("Digite su numero:"))

if numero > 0:
    print("su numero es positivo")
elif numero == 0:
        print("su numero es igual a 0")
else :
    print("su numero es negativo")

#hacer un programa que pida 3 numeros y determina cual es el mayor

num1 = int(input("Digite su primer numero"))
num2 = int(input("Digite su segundo numero"))
num3 = int(input("Digite su tercer numero"))

if num1 > num2 and num1 > num3 :
     print(f"el numero mayor es:{num1}")
elif num2 > num1 and num2 > num3 :
    print(f"el numero mayor es: {num2}" )
elif num3 > num1 and num3 > num2 :
    print(f'el numero mayor es {num3}:')
else:
    print("ningun numero es mayor")

