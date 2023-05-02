import pyautogui
import time
import webbrowser
import numpy

numero_telefono = '+57 3123113498'

msm = open('mensajes.text')
mensaje = []
for i in msm:
    if i != '/n':
        mensaje.append(i)

print(len(mensaje))

n = np.random.randint(0,83)


url = 'https://www.web.whatsapp.com/send?phone='
webbrowser.open(url + numero_telefono)
time.sleep(8)
pyautogui.write(mensaje[n])
pyautogui.press('Enter')
