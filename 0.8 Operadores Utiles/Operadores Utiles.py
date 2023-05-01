
"""nos imprimira del 1 al 10  nuestra lista xd  le podemos 
poner una , para ver desde donde inica y  hasta que numero termina 
o podemos saltar de dos en dos poniendo una coma estra y el numero que deseamos saltar"""
milista = [1,2,3]
for i in range (1,11,2):
    print(i)


print(list(range(0,11,2)))

# Contador 
 
contador_indice = 0
palabra = "hola"

for letter in palabra :
    print(palabra[contador_indice])
    contador_indice += 1

for  item in enumerate(palabra):
    print(item)

for index,letter in enumerate(palabra):
    print(index)
    print(letter)
    print("\n")