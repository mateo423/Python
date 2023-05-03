# Ejemplo 1
def func(*args):  # usando args podemos usar mas argunmentos
    return print(sum(args) * 0.05)


func(40, 50, 60, 230, 4540)


# Ejemplo
def funcion(**kwargs):
    # creamos una funcion que tegan kwargs para poner varios argumentos
    if "fruta" in kwargs:
        # lo segundo creado un if si fruta esta en el kwargs
        print("mi fruta escogida es {}".format(kwargs["fruta"]))
        # aca imprimimos si fruta es kwargs  estamos buscando fruta
    else:
        print('No hay fruta')


# aca llamamos nuestra funcion
funcion(fruta="manzana", vegetales="lechuga")
