"""Ejercicio 2: Sumar elementos de una lista
Dada una lista de números, calcula la suma de todos los elementos."""

numeros= [1, 2, 4, 6]

suma = 0

for numero in numeros:
    suma += numero
    print(f'la suma de la lista es {suma}')