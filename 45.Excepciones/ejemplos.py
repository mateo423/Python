
try:
    # si utlizas el atributo 'r' es para leer archivo 
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()

# si intentas abrir el archivo.txt  si el archivo no existe se capturara el FileNotFoundError
except FileNotFoundError:
    print('Erro el archivo no existe')

# si hay un error de entrada y salida de el archivo se ejecutara el OSError y se emprime el mensaje de error
except OSError:
    print('Erro de entrada/salida del archivo')
    