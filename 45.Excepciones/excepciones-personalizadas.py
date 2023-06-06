# excepciones personalizadas para manejar situaciones específicas en tu código. Para hacerlo, debes definir una clase que herede de la clase base Exception o una de sus subclases.

class miexepcion(Exception):
    pass

try:
    #Codigo que pueda generar una excepcion personalizada 
    raise('Este es un mensaje de erro personalizado')

except miexepcion as e :
    #Manejo de la excepcion personalizada
    print(e)

# except captura la excepción y muestra el mensaje de error personalizado.