 # While
 
 # Palabras Clace Utiles
 # break
 # continue
 # pass
 

x = 0
while x < 5:
 print(f"su valor actual es {x}")
 x += 1
else :
    print("Error x no es mayor a 5")

x = [1,2,3]

# Ejemplo con el pass

# el pass es para pasar ala otro linea de code xd 
for item in x :
    #Comentario
    pass
print("Fin del libro ")

# Ejemplo con el continue

# el continue nos indica que continuamo sin una letra que es la "e" y nos imprimira "mato"
b = "mateo"

for letter in b :
    if letter == 'e':
        continue
    print(letter)

# Ejemplo con el break

# break para  desde donde le indicamos  que es la "a" rompe  la variables algo asi xd
v = 'mateo'

for letter in v :
    if letter == 'a':
        break
    print(letter)
