# hacer un programa donde la edad de 18 es mayor de edad y menor de edad

edad = int(input('digite su edad'))

if edad > 0 and edad > 18 and edad <100:
    print("eres mayor de edad")
elif edad > 0 and edad < 18:
    print('eres menor de edad')
elif edad == 18:
    print("su edad es 18")
elif edad > 100 :
    print("usted no puede tener esa edad en la tierra")
else :
    print("su edad es incorrecta")
