


mi_lista2 = ['mateo','cristian','josue','estela']
mi_lista = ["castro", 'pedroza']


# Como tal se puede almacenar y crear una nueva variable que almacene las 2 variables para sumarla
nueva_lista = mi_lista2 + mi_lista
print(nueva_lista)

# le estamos indicando que el primer numero de la lista se va a cambiar  a string que les estamos indicando
# osea 'mateo'
# tambien se puede concatenar con la funcion .append

nueva_lista [0] = 'mateo'
print(nueva_lista)

# concatenamo para agregar  digamos otro elemento
nueva_lista.append('seis')
print(nueva_lista)

# tambien podemos remover elemento de una lista con una funcion  pop
# y le podemos asignar un numero para quitar la variable osea 0 y se nos quitara el elemento 'mateo'

nueva_lista.pop()
print(nueva_lista)

# ahora donde va este numero que sacamos nosotros podemos guardarlo en una variable
item_popeado = nueva_lista.pop(0)
print(item_popeado)

