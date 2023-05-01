num1 = int(input('ingrese el numero'))
num2 = float(input('ingrese el siguente numero'))

# si cualquier numero es divido entre dos y su residuo es igual a cero eso significa que el numero es par
if num1 %2 == 0 and num2 %2==0:
    print('los numeros son par')
elif  num1 %2== 0 and num2 %2 !=0:
    print('el primer numero  no es par')
    print(f'{num1} es par')
else:
    print('ningun numero es par')