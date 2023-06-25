import tkinter

ventana = tkinter.Tk()
ventana.geometry('400x300')

#BOTTONS

def saludo():
    print('hola')


boton1 = tkinter.Button(ventana, text = 'presiona', command=saludo)
boton1.pack()

#ETIQUETAS

#etiqueta = tkinter.Label(ventana, text ='hola mundo', bg='Blue')
#etiqueta.pack(fill= tkinter.BOTH, expand= True)

ventana.mainloop()
