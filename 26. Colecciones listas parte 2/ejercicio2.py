"""Escriba un programa que tenga dos listas y que, a continuacion, cree las
sigeuntes listas (en las que no debe haber repeticiones):

- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas.
"""

lista1 = ['mateo', 'sofia', 'keivn', 3, 5, 7]
lista2 = ['cristian', 'estela', 'ever', 5, 6, 9, 0 ]


a = set(lista1)
b = set(lista2)

union = list(a | b)

listaA = list(a - b)


listaB = list(b - a)

interseccion = list(a & b)

print(f'lista de elementos que aparecen en las dos listas \n {union}')
print(f'lista de elementos que aparecen en la primera lista, pero no en la segunda \n {listaA}')
print(f"lista de elementos que aparecen en la segunda lista, pero no en la segunda \n {listaB}")
print(f"lista de elemntos que aparecen en ambas listas : {interseccion}")