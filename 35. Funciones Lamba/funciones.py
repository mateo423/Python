
# Creamos una lista
mi_lista  = [1, 2, 3, 4]

#  creamos una funcion llmada square y que tengan un variable llamda num1
def square(num1):
    # definimosy creamos otra variable llamada resultado es igual que la variable num1 al cuadrado
   resultado = num1 **2
   # decimos que nos devolvera el resultado
   return (resultado)

# 
for item in map(square,mi_lista):
    print(item)
    