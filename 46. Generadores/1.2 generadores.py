def contar_hasta(n):
    i = 0
    while i < n:
        yield i
        i += 1

generador = contar_hasta(5)
for numero in generador:
    print(numero)
