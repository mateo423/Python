def sumar(num1,num2):
    return num1+ num2

def restar(num1,num2):
    return num1- num2

def Multiplicar(num1,num2):
    return num1* num2

def division(num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return 'Operacion Erronea'    

def redondeo(num1,num2):
    return num1//num2

while True:
    try: 
        op1 = int(input('Ingrese el primer numero :'))
        op2 = int(input('Ingrese el seguno numero :'))
        break
    
    except ValueError:
        print('Los valores no son correctos. Intentalo de nuevo')
    
operacion = input('Ingrese la operacion que deseas relaizar : \n 1.suma \n 2.resta\n 3.multiplicacion \n 4.division \n 5.redondeo\n Cual de estas operacion deseas : ')
 
 
if operacion == "suma":
    print(sumar(op1, op2))

elif operacion == 'resta' :
    print(restar(op1, op2))

elif operacion == 'multiplicacion':
    print(Multiplicar(op1, op2))

elif operacion == 'division':
    print(division(op1, op2))

elif operacion == 'redondeo' :
    print(redondeo(op1, op2))

else:
    print("Acurrido Un Error de Ejecucion Ingrese otra vez los valores ")
    
print('Operacion ejecutada. Continuacion de ejecucion del Programa')