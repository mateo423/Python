"""Escriba un programa donde tenga una lista y que, a continuacion, elimine 
los elementos repetivos, por ultimo mostrar lista """

lista = ['mateo', 2, 3, 4, 'sofia', 'kathe', 'ever', 'estela',4, 4, 4, 1, 2, 4, 6, 7, 65, 7]

conjunto = set(lista)
lista = list(conjunto)
print(lista)

lista2 = [1, 1, 1, 3, 4, 5, 3, 5, 4, 4, "mateo", 'mateo', 'sofia', 'josue']

lista2 = list(set(lista2))
print(lista2)
