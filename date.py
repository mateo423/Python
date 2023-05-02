import requests
from bs4 import BeautifulSoup

"""Basicamente este es un ejemplo sencillo en un web Scraping
1. buscamos una pagina web
2. extraemos el html
3. lo convertimos a un formato que python lo pueda manejar
4. buscamos junto el contenido que creemos y  lo escribimos en algun lado
o lo procesamos 
"""
url = 'https://www.frasess.net/frases-romanticas-para-enamorar-71.html'
pagina = requests.get(url)

bs = BeautifulSoup(pagina.content, 'html.parser')
mensaje = bs.find_all('div', class_="quote_text")

texto = open("mensaje.text", "w")

for i in mensaje:
    texto.write(i.text)
