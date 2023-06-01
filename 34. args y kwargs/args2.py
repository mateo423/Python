def alumnos_profesores(profesor, sustitulo, *args):
    print('Profesor' + profesor)
    print('Sustituto :' + sustitulo)
    for x in args:
        print('alumnos :',x)

lista_alumnos = ('Andres', 'ana','camila')

lista_profesores = ("Antonio" 'mateo', *lista_alumnos)
