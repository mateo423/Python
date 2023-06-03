"""Las variables definidas dentro de una cuncion tienen un abmito local
lo que significa que solo son accesibles dentro de esa funcion.
Sin embargo, tambien puedes acceder a variables definidas fuera de una 
funcion dentro de la funcion utlizando la palabra clave global """

x = 5


def imprimir_x():
    global x
    print(x)


imprimir_x()
