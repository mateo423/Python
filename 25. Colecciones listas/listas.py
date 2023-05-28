# en las lista como tal se le puede agregar el slancig o el len
# creamos una lista normal con strign y numeros hasta puede ser flooad
mi_lista = ['Mateo',2,3]
print(len(mi_lista))

# estamos imprimiento el valir de la lista 0 osea que es 'mateo'
print(mi_lista[0])

#
print(mi_lista[1:])

# creamos listas
mi_lista2 = ['cuatro', 'sinco','sei']
mi_lista3 = ['siete','ocho']

# sumamos la listas y las imprimimos
print(mi_lista2 + mi_lista3)


#en las lista como tal se le puede agregar el slancig o el len 
mi_lista = ['Mateo',2,3]
print(len(mi_lista))
#
print(mi_lista[0])
#
print(mi_lista[1:])

mi_lista2 = ['cuatro', 'sinco','sei']
mi_lista3 = ['siete','ocho']
print(mi_lista2 + mi_lista3)
#Como tal se puede almacenar y crear una nueva variable que almacene las 2 variables para sumarla
nueva_lista = mi_lista2 + mi_lista3
print (nueva_lista)
#le estamos indicando que el primer numero de la lista se va a cambiar  a string que les estamos indicando 
#osea 'mateo'
'tambien se puede concatenar con la funcion .append'
nueva_lista [0] = 'mateo'
print(nueva_lista)
#concatenamo para agregar  digamos otro digito 
nueva_lista.append ('seis')
print(nueva_lista)
#tambien podemos remover elemento de una lista con una funcion  pop
nueva_lista.pop()
#y le podemos asignar un numero para quitar la variable osea 0 y se nos quitara el elemento 'mateo'
print(nueva_lista)
#ahora donde va este numero que sacamos nosotros podemos guardarlo en una variable 
item_popeado = nueva_lista.pop(0)
print(item_popeado)

# Es una forma de crear una lista
lista23 = list("1234")
print(lista23)

# Una lista se puede crear utilizando[]

lista = [1, 'mateo', 3.45, [1, 5, 6]]
print(lista)

# Como acceder a listas 

lista_por_modificar = [1, 2, 'Mateo', 3.1416, 5, 4, 6, 7, 8]
print(lista_por_modificar[-1])
print(lista_por_modificar[1])
print(lista_por_modificar[2])
print(lista_por_modificar[3])

# Modificar un elemento de una lista 

lista_por_modificar[2] = 1
print(lista_por_modificar)

# Eliminar elemento de una lista

del lista_por_modificar[0]
print(lista_por_modificar)

# Creacion de Sublistas 

print(lista_por_modificar[2:8])

# modificar y agregar nuevos valores utilizando el :

l = [1, 2, 3, 4, 5, 6]
# que la ista l inicie desde el numero 1 y terminer hasta el 5
l[6:0] = [0, 0, 0,]
print(l) #[0, 0, 0, 4, 5, 6]

#

s = [1,4,5]
x, y, z = s
print(x, y, z)


# iterar listas 
listasks = [1 ,4 ,5 ,6]
for i in listasks:
    print(listasks)

# si necesitamos un index acompa;ado de la lista es como un contador 

listasks = [1 ,4 ,5 ,6]
for index in enumerate (listasks):
    print(index,listasks)
    
# O si tenemos 2 lista y la deseamos iterar podemos hacerlo 
lista1 = [2, 3, 4, 6, 7]
lista2 = [1, 5, 7, 95, 7, 'hola']

for l1, l2, in zip(lista1,lista2):
    print(l1,l2)
    
# Tambien podemos utilizar una longitud sobre una lista 

for i in range(0, len(lista1)):
    print(lista1[i])

# Metodos de listas

# .append sirve para agregar un elemento a una lista

listas40 = [1, 4, 5, 6, 8]
listas40.append(6)
print(listas40)

# sirve para quitar un elemento de una lista

listas40.pop(0)
print(listas40)

# sirve para a;adir un elemento en una posicion o indice determinado
# el primer numero es donde incial  el segundo numero es que queremos insertar 
listas40.insert(4,5)
print(listas40)

# Sirve para remover un elemento de una lista
listas407 = [1, 2, 3]
listas407.remove(1)
print(listas407)

listas407.append(8)

# sirve para invertir la lista

listas407.reverse()
print(listas407)

#sirve para organizar el elemento por mayor y menor

listas407.sort()
print(listas407)

# Tambien permite ordenar de mmayor a menor si se pasa como parametro 
ka = [3, 2, 1, 4, 5, 6, 7]
ka.sort(reverse=True)
print(ka)

# nos indica que numero esta indicado el elemento que queremos xd 
ma = ['mateo', 'castro', 'pedroza']
print(ma.index('castro'))

ki = [1, 1, 1, 1, 2, 1, 4, 5]
print(ki.index(2,3))
