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