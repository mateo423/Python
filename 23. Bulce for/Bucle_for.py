"""los bucles for sirven para reptir tipo de numeros elige cada item y ese lo repite
 se pueden hacer con string con diccionarios con tuplas tambien"""

diccionario = {"manazana": 2.40, "Uva": 5.60}

for i in diccionario:
    print(diccionario)

# se puede hacer con listas

coleccion = [2, 1, 3, "juan"]

for i in coleccion:
    print(i)

milista = [1,2,3,4,5,6,7,8,9,10]

for jamon in milista:
    if jamon % 2==0:
        print(jamon)
        
    else:
        print(f'si no es par {jamon}')
        
       