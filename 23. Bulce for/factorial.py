# Factorial Es el producto de todos los numeros positivos enteros comprendidos entre 1 y un 

# factorial de 5 : 1 * 2 * 3 * 4 * 5 
# facotiral de 5 : 1 * 2 * 3 * 4 * 5 


numero= int(input('Ingrese su numero : '))

factorial = 1

for n in range(1,(numero+ 1)):
    factorial = factorial * n

print('El factorial de {0} es : {1}'.format(numero,factorial))
