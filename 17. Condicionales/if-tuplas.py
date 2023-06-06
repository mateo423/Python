print('--- Crusos ---')
print('Matematicas', 'Biologia', 'Lenguaje', "Ciencias")

cursos = input('Ingrese el grupo que desea : ')

if cursos in ('Matematicas,', 'Biologica', 'Lenguaje', 'Ciencias'):
    print('Crso (0) seleccionado'.format(cursos))
    
else: 
    print('No exiten eso cursos')
    