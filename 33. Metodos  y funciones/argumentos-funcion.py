"""Las funciones pueden tener argumentos opcionales nos ayuda  a que la funcion
sea mas flexible"""


def saludar(nombre, saludo='Hola'):
    print(saludo,nombre)

saludar('juan')
saludar('hola como te va xd', 'Hola buenos dias')
