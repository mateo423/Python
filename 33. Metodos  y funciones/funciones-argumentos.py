def suma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
        return numero


resultado = suma(3, 5, 6, 8)
print(resultado)
