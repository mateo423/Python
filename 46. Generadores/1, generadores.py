# Los generadores permiten extraer valores de una cuncion y almacenarlo de uno en uno) en objetos iterables (que se pueden recorrer),
# sin la necesidad de almacenar Todos ala vez en la memoria RAM


"""
def generaMultiplo7(limite):
    numero = 1
    listaNumeros = []
    
    while numero<=limite:
        listaNumeros.append(numero*7)
        numero = numero + 1
    return listaNumeros # Retorna toda la lista creada 

print(generaMultiplo7(2))
"""


def generaMultiplos7(limite):
    numero = 1
    listanumeros = []
    
    while numero<= limite:
        yield numero * 7 # cede la intruccion "yield" genera un objeto iterable
        numero = numero + 1

obtienemultiplos7 = generaMultiplos7(10)

"""for i in obtienemultiplos7:
    print(i)"""


#Next() : Retorna el siguente elemento de un objeto iterable:

print(next(obtienemultiplos7))
print('Aca hay 100 lineas de codigo ')
print(next(obtienemultiplos7))
print('Aca hay 100 lineas de codigo ')
print(next(obtienemultiplos7))
print('Aca hay 100 lineas de codigo ')
