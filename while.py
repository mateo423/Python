'''
Bucle while  es un trozo de codigo que se va  repetir un numero indeterminado solamente 
es algo que se va a repetir a repetir
'''
# solo necesitamos que se cumpla una  condicion 
# para que el bucle se siga ejecutando 

#Este módulo proporciona acceso a las funciones matemáticas definidas
import math

numero = int(input("Digite su numero -> "))

# while es mientras se cumpla una condicion
#el bucle se va a seguir ejecutando
while numero < 0 :
    print('error -> el numero debe de ser positivo')
    numero = int(input('Digite su numero -> '))
    
print(f'/nSu raiz cuadrada es ->  {(math.sqrt(numero)):.2f}')

# Otro ejemplo 

#creamos una variable llamada i
i = 1

# while  -  condicion i < 5 :
while i < 5:
    print(i)

#agrega numero
    i += 1