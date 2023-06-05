
"""Los set en Python son un tipo que permite almacenar varios elementos y acceder a ellos de una 
forma muy similar a las listas pero con ciertas diferencias
sets es una coleccion unica y Desordenada de elementos
Solamente puede haber UNA representacion del mismo objeto 
estos no pueden ser duplicados. """


# 1 .Creacion de un conjunto 

print('1. Creacion de un conjunto')


#Nota: En conjunto no existe elementos duplicados 

# Manera de Crear un conjunto
conjunto_1 = {'juan', 'daniela', 'juan', 'camila', 'pablo', 'camila'}

conjunto_2 = set(['juan', 'daniela', 'juan', 'camila', 'pablo', 'camila'])



print(f'Contenido de la variable conjunto 1 :  {conjunto_1}')
print('El Tipo de dato es : ', type(conjunto_1))
print(f'Contenido de la variable conjunto 2 :  {conjunto_2}')
print('Contenido de la variable conjunto 2 : ', "y tenemos", len(conjunto_2), 'Conjuntos' )
