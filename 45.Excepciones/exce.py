"""supongamos que nuestro programa tiene que procesar cierta información ingresada
por el usuario y guardarla en un archivo. Dado que el acceso a archivos puede levantar excepciones,
siempre deberíamos colocar el código de manipulación de archivos dentro de un bloque try.
Luego deberíamos colocar un bloque except que atrape una excepción del tipo IOError,
que es el tipo de excepciones que lanzan la funciones de manipulación de archivos. 
Adicionalmente podríamos agregar un bloque except sin tipo por si surge alguna otra excepción. 
Finalmente deberíamos agregar un bloque finally para cerrar el archivo, haya surgido o no una excepción.
"""

# ---- Bloque ----

archivo = None # Archivo None  signifca que esta vacido 
try:
    archivo = open("archivo.txt")
    # procesar el archivo
except OSError:
    print("Error de entrada/salida.")
    # realizar procesamiento adicional
except Exception as e:
    print('Ocurrio una exception', str(e))
    # procesar la excepción
finally:
    # si el archivo no es None y no esta cerrado, hay que cerrarlo
    if archivo is not None and not archivo.closed:
        archivo.close()
