"""Ejercicio 4: Contar vocales en una cadena
Dada una cadena de texto, cuenta el número de vocales (a, e, i, o, u) que contiene."""

bocales = 'a e i o u '
contador = 0

for i in bocales:
    contador += i
    print(contador)