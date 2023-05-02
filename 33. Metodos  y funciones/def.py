
def decir_hola():
  print('hola')
  print('como estas')
  
decir_hola()


def ingrese_su_nombre(nombre):
    print(f' hola {nombre} encantando de saludarte')


ingrese_su_nombre(nombre=input("como te llama > "))

# funcion de sumar 
def suma (num1, num2):
  total = num1 + num2
  print(total)
  
suma (1,2) 

def nombre_y_edad_y_cuidad_y_telefono_apellido(nombre, apellido, cuidad, telefono, edad):
    print(
        f'soy {nombre} y mi apellido es {apellido} y vivo en {cuidad} mi telefono es {telefono} y tengo {edad} años '
        f'de edad')


nombre_y_edad_y_cuidad_y_telefono_apellido("sofia", "castro", "cali", 3123113498, 14)

