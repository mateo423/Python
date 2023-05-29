try:
    dividendo = float(input("Ingrese el primer numero que desea dividir : "))
    divisor = float(input("Ingrese el siguente numero para terminar la division : "))
    division = dividendo / divisor
    print(f"La division de los dos numero que ingreso son {division}")
except ValueError:
    print("error el numero que ingreso  no ce permite string")
    
except ZeroDivisionError:
    print('Error no se puede dividir entre 0')