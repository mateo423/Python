
import time 

def obtener_datos_De_api():
    # intentar obtener los datos API
    intentos = 3
    tiempo_de_espera = 5
    for _ in range(intentos):
        try:
            # Codigo para obtener los datos API
            datos = obtener_datos_De_api()
            return obtener_datos_De_api
        except ConnectionError:
            #Manejo de la exepcion de conexion
            print("Error de conexion. Vuelva e intentar en {} segundos".format(tiempo_de_espera))
            time.sleep(tiempo_de_espera)
        
        print('No ce pudo obtener los datos despues de {} intentos'.format(intentos))
        return None