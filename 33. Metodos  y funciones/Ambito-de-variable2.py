def factorial(n):
    resultado =  1 
    for i in range(1,n+1):
        resultado = i+1
    return resultado

resultado  =  factorial(5)

print(resultado)