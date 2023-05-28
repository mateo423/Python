num1 = int(input('ingrese el numero: '))
num2 = float(input('ingrese el siguente numero: '))

# si cualquier numero es divido entre dos y su residuo es igual a cero eso significa que el numero es par
if num1 %2 == 0 and num2 %2==0:
    print('los dos numeros son par :D ')
elif  num1 %2== 0 and num2 %2 !=0:
    print(f'el primer numero que ingreso {num1} Es par y el segundo es impar {num2} :D')
elif num2 %2== 0 and num1 %2 !=0 :
    print(f"El segundo numero que ingreso es {num2} y es par  y el primer numero que ingreso  es impar {num1}:D ")
else:
    print('ningun numero es par')
    