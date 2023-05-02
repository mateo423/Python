from random import shuffle, randint


milista1 = [1, 2, 3, 4, 5, 6,7,8,9,10]
mimlista2 = ['a','b','c']
b = {'ki': 1} # diccionario
milista3 = [100, 200, 300]

# el zip sirve para emparejar una lista con la otra 
for item in zip(milista1,mimlista2,milista3):
    print(item)
    
print(list(zip(milista1, mimlista2, milista3)))

# con diccionario xd 
if 1 in b.keys():
    print("Su resultado es verdadero")

# el valor min = el valor minimo xd  de la variable

else:
    print("False")
print(min(milista1))

# el valor maximo xd 
print(max(milista3))
# shuffle una funcion que se tiene que correr en linea digamos en la consola o en idl de python
# tambien es para randint escoger cualquier numero aleatorio desde la consola tambien es lineal

# hacer que un numero se combierta en un float o en int
resultado = input("Escribe un numero aqui-> ")

print(type(float(resultado)))
