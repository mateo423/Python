""" 1. - realizar una solicitud a una API web y obtener los datos en formato JSON.
    2. - Si se produce un error al realizar la solicitud, se captura la excepción requests.exceptions.RequestException y se imprime un mensaje de error detallado.
    3. - Si hay un error al procesar la respuesta en formato JSON, se captura la excepción ValueError y se imprime un mensaje de error correspondiente."""


import requests

try:
    respuesta= requests.get("https://www.ejemplo.com/api/datos")
    datos = respuesta.json()
    print(datos)
except requests.exceptions.RequestException as e:
    print("Ocurrio un error de solucitud ", str(e))
except ValueError:
    print('Eror al procesar la respuesta en formato.JSON')

