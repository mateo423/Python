"""Si te encuentras usando un ciclo for con .append() para crear una lista
puedes usar una comprehension en su lugar"""

mi_cadena = 'hola'

mi_lista = []

for letter in mi_cadena:
    mi_lista.append(letter)
        
print(mi_lista)

# Otra manera  de hacerlo xd 
milista = [x**2 for x in range(0,11)]
print(milista)

Celcius = [0,10,20,34.4]

fahrenheit = [((9/5)*temp + 32) for temp in Celcius]
print(fahrenheit)
#Otra forma

fahrenheit = []

for temp in Celcius:
    fahrenheit.append(((9/5)*temp + 32))