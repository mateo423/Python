mi_diccionario = {
    'manzana': '2.90', 'mango': "1.80", "naranja": "2.30"
}
print(mi_diccionario['manzana'])

# aca  en los diccionarios trabajos llaves y valor
# Tambien podemos cuardar listas  Por ejemplo

mi_segundo_diccionario = {
    'tomate' : '2.90', 'keke': ['manzana', 'platano','Pepino'], 'leche' : '2.90'
}
#  esto es un claro ejemplo por que en primer lugar debemos que habrir braques cuadrados a kakes
#por que el como la puerta y  nosotros creamos una lista dentro keke para poder abrilar necesitamos
#habrir otro braques cuadrado peero esta vez vamos indicar el numero que deseamos ver en pantalla
# el numero 1 es el platano directamente nos imprimira el platano


print(mi_segundo_diccionario['keke'][1])

mi_otra_lista = {
    'manzana' : '2.90', 'kekes' : '2.90'
}
#esto podemos sobre escribirlo hacer que cambie  por jeemplo vamos a indicarle que 
#kekes es igual que 300
mi_otra_lista['kekes'] = 300
print(mi_otra_lista)


#si queremos ver  todas las llaves que se encuentra en el diccionario 
#pordemos decir keys

mis_lista = {
    'manzana' : '2.90', 'kekes' : '2.90'
}
print(mis_lista.keys())

# o si queremos que solo nos den los valores utilizamos values
print(mis_lista.values())