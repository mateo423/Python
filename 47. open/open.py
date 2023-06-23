
nombre_archivo = 'menssage.txt'
 
with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola mundo')

with open(nombre_archivo, 'a') as archivo:
    archivo.write('\n Fin del hola mundo')

print('Se a escrito correctamente en el archivo')
