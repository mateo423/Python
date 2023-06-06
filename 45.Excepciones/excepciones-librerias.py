import time
import requests

def obtener_datos_de_api(url, intentos=3, tiempo_de_espera=5):
    for _ in range(intentos):
        try:
            # Código para obtener datos de una API
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción si hay un error en la respuesta
            return response.json()
        except (requests.RequestException, ValueError) as e:
            # Manejo de excepciones de red o error de análisis JSON
            print("Error al obtener datos de la API:", str(e))
            print("Reintentando en {} segundos...".format(tiempo_de_espera))
            time.sleep(tiempo_de_espera)
    
    print("No se pudo obtener los datos después de {} intentos".format(intentos))
    return None
