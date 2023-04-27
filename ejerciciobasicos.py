# hacer un programa donde la edad de 18 es mayor de edad y menor de edad

edad = int(input('digite su edad'))

if 0 < edad < 100 and edad > 18:
    print("eres mayor de edad")
elif edad < 0 < 18:
    print('eres menor de edad')
elif edad == 18:
    print("eres mayor de edad 18")
elif edad > 100:
    print("usted no puede tener esa edad en la tierra")
else:
    print("su edad es incorrecta")


# Hacer que pida un caracter e indiquue si es una vocal o no

letra = input('Digite su caracter')
letra = letra.lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('el caracter que ha colocado es una vocal')
else:
    print('esto no es una vocal sapa')
