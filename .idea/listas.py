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