"""Programa que toma los tres notas de un estudiante y diga la nota final del curso.
Tenga en cuenta que la primera y segunda nota valen el 30% de la nota final- la tercera nota vale el 40%"""

# Primero ingresamos una funcion nombrada calcularnota
def calcularNota(nota1,nota2,nota3):
# dentro de hecha tenesmos unas variables 
    return(nota1 *0.3)  + (nota2 *0.3) + (nota3 *0.4)
# nos va a devolver nota * 0.3 ya que es el 30% la ultima nota es del 40% osea 0.4

# las variables donde vamos ingresar  las 3 notas del curso
nota1 = float(input("Ingrese la primera nota"))
nota2 = float(input("Ingrese la segunda nota"))
nota3 = float(input("Ingrese la tercera nota"))

"""Creamos una variables que tenga almacenado nuestra funcion
y las variables de las notas"""
NotaFinal = calcularNota(nota1, nota2, nota3)

# Despues imprimimos  el resultado de las notas 
print("Su nota final del curso es : ", round, NotaFinal,2)