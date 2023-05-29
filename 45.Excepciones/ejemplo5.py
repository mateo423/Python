while True:
    try:
        edad = int(input("Ingrese su edad : "))
        if edad > 18 and edad < 100:
            print("Eres mayor de Edad")
        elif edad == 18:
            print('Eres mayor de edad')
        elif edad > 0 and edad < 18:
            print('Eres menor de edad')
        elif edad < 0:
            raise ValueError("Error No existe una edad negativa en la tierra")
        elif edad > 100 :
            raise ValueError("Esa edad no se encuentra en tierra")
        break
    except ValueError as e:
        print('Error el  no se permite string no digite nada de palabras por fa ', str(e))
