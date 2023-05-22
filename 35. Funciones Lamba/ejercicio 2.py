"""Escriba un programa que verifique si un número es primo o no. Por ejemplo, para los número 3, 5, y 13, la variable primo debe 
ser True, y para 1, 10, y 33, False."""

def es_primo(numero):
  primo = True
  if primo == 1 :
    return False
  if primo == 2:
    return True
  else:
      for i in range(2,numero):
        if numero %i == 0 :
            return False 
  # aquí debes implementar tu código
  # modificando la variable primo 
  # (no modifiques nada de las lineas anteriores)
  return primo
