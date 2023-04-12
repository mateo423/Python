''' operador AND : en los operadores logicos el AND  cualquier  operador que tenga false su resultado
va hacer false digamos que el false vale 0 y el true vale 1 cualquier resultado de 0 va a dar 0
 y cualquier resultado de 1 va hacer el mismo numero osea que es true 

 True AND True resultado = True
 True AND False resultado = False
 False AND True resultado = False
False AND False resultado = False


 operador OR :  bueno en el operador or es muy diferente ya que parece una suma
es decir  si el resultado es menos va hacer positivo es decir que si  sumamos el false
con el true va ahcer positivo  asi mismo al revez la unica manera que  el resultado es negativo
 es tener 2 negativo osea False OR False Resultado = False
  esto son los ejemplos

True or true  resultado = true
false or true resultado = true
true or false resultado = true
false or false resultado = false
''' 




a = 10
b = 12
c = 13
d =10
((a>b) or (a<c)) and ((a==c)) or (a>=d)
#   f        t           f          f 
#       t         and     false
#               false