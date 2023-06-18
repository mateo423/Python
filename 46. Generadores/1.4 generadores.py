def retorna_cuidades(*ciudades):
    for elementos in ciudades:   #For anidado entramos en los sub elementos que tiene elemento 
        for sub_elemento in elementos:    
            yield sub_elemento
    
ciudades_retornadas = retorna_cuidades('Madri', 'Cairo', 'Cali', 'Bogota', 'San jose', 'Tolima')

print(next(ciudades_retornadas))

#ejemplo con el yield from  es el mismo resultado pero con el codigo simplificado 

def retorna_Animales(*Animales):
    for elementos in Animales:
        yield from elementos

Animales_retornados = retorna_Animales('Gallina', 'perro', 'Conejo', 'Leon', 'Oso')

print(next(Animales_retornados))
