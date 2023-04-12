#permite construir expresiones logicas se obtiene como resultado booleanos

# a=10 b=12  c=13  d=10
#((a>b))or(a<c))and((a==c)or(a>=b))
    # F or  T   and    F   or    F
    #    T      and         F
                #F
#Prioridad de los operadores en general
#1. ()
#2. **
#3. *, /, mod, not
#4.+, -, and
#5.>,<, ==, >=, <=, !=, or

#Permite construir operaciones logicas que dan resultados boleaano
'''
operador AND : en los operadores logicos el AND  cualquier  operador que tenga false su resultado
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

Operador Negacion :
este operador si esta en true el resultado va hacer negativo pero si 
esta en negativo va estar positivo

not(true) 
not(false)

'''

a=10
b=15
c=20
resultado = ((a>b) and (a<c))
print(resultado)

resultado1 = ((c>b) and (a<c))

print(resultado1)

resultado12 = ((c==b) and (a*c==b))

print(resultado12)

adc= 2000
fgh = 300
jkl=5000


operadores = ((adc*4-jkl==fgh) and (fgh+jkl-2000,fgh>jkl))
print(operadores) 

