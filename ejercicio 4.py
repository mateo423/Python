#Ejercicio 4
'''
 hacer un programa para ingresar el radio de un circulo y se 
 reporte su area y la longitud de la circunferencia 
'''
import math # para importar el valor pi 
radio = float(input("radio =>"))

area = math.pi * radio**2
longitud = 2 * math.pi* radio

print(f"el area del circulo es : {area:.2f}")  #le estamos indicando que queromos solamente dos decimales 
print(f"la longitud de la circunferencia es: {longitud:.2f}")


