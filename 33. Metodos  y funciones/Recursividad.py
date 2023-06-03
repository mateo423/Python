"""Es un concepto donde la funcion se llama asi misma 
Esto sucede cuando quiere resolver un ejercicio"""


def factorial(n):
    if n == 0:
        return 1 
    else: 
        return n * factorial(n - 1)

resultado = factorial(5)

print(resultado)
