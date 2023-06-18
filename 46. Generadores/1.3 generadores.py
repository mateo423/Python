def Funcion_pares(limite):
    num = 1
    
    miLista = []
    
    while num < limite:
        miLista.append(num*2)
        
        num = num+1
    
    return miLista

print(Funcion_pares(10))

#Ahora con con yield que utilizan los generadores 

def Genera_pares(limite):
    
    num1 = 1
    
    while num1<limite:
        yield num1*2
        num1 = num1+1
#suspension 
devuelve_pares = Genera_pares(10)

print(next(devuelve_pares))

print('Aqui podria ir mas codigo ...')

print(next(devuelve_pares))
print('Aqui podria ir mas codigo ...')

print(next(devuelve_pares))
print('Aqui podria ir mas codigo ...')

print(next(devuelve_pares))
print('Aqui podria ir mas codigo ...')

print(next(devuelve_pares))
print('Aqui podria ir mas codigo ...')
