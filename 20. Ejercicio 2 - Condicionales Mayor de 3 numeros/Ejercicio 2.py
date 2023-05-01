#Ejercicio  hacer un programa donde el numero que ingrese sea mayor al otro XD algo asi 

num1 = int(input("Ingrese su numero -> "))
num2 = int(input("Ingrese su numero -> "))
num3 = int(input("Ingrese su numero -> "))

if num1 >= num2:
    print(f"su numero mayor es -> {num1}")
elif num2 >= num3:
    print(f'El numero mayor es -> {num2}')
elif num3 >= num1:
    print(f"El numero mayor es -> {num3}")
elif num2 >= num1:
    print(f"El numero mayor es -> {num2}")
else:
    print("Error")