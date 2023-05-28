# Hacer que pida un caracter e indiquue si es una vocal o no

letra = input('Digite su caracter: ')
letra = letra.lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('el caracter que ha colocado es una vocal')
else:
    print('esto no es una vocal sapa')
