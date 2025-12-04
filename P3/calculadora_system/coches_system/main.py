

from view import vista
from tkinter import *

class App:
    def __init__(self,ventana):
        view=vista.Vistas(ventana)


if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()

"""
implementacion mvc
poo
interfaces:
3.1 menu principal *()
3.2 menu acciones *()
3.3 insertar autos()
3.4 consultar autos()
3.5 cambiar autos()
3.6 borrar autos()

productos entregables:
estructura del proyecto basado en mvc
modulo principal "main"
interaccion con las interfaces
nombre del commit: commit_01_12_25

insertar_camionetas
consultar_camionetas
cambiar_camionetas
borrar_camionetas
insertar_camiones
consultar_camiones
cambiar_camiones
borrar_camiones
"""