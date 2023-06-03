def alumnos_profesores(profesor, sustitulo, *args):
    print('Profesor' + profesor)
    print('Sustituto :' + sustitulo)
    for i in args:
        print('alumnos :', i)


lista_alumnos = ('Andres', 'ana', 'camila')

lista_profesores = ("Antonio" 'mateo', *lista_alumnos)
