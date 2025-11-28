from tkinter import messagebox
from model import operaciones
from view import interfaz


class Controladores:
    @staticmethod
    def operaciones(titulo,numero1,numero2,signo):
        if signo=="+":
            resultado=numero1+numero2
        elif signo=="-":
            resultado=numero1-numero2
        elif signo=="x":
            resultado=numero1*numero2
        elif signo=="/":
            resultado=numero1/numero2
        #messagebox.showinfo(icon="info",title=titulo,message=f"{numero1}{signo}{numero2}={resultado}")
        resul=messagebox.askquestion(title=titulo,message=f"{numero1}{signo}{numero2}={resultado} \n¿Quieres guardar la operacion en la base de datos?",icon="question")
        if resul=="yes":
            respuesta = operaciones.Operaciones.insertar(numero1,numero2,signo,resultado)
            Controladores.respuesta_sql("Agregar registro", respuesta)

    @staticmethod
    def eliminar(id):
        repuesta = operaciones.Operaciones.eliminar(id)
        Controladores.respuesta_sql("Borrar registro", repuesta)

    @staticmethod
    def cambiar(num1,num2,signo,resultado,id):
        repuesta = operaciones.Operaciones.actualizar(num1,num2,signo,resultado,id)
        Controladores.respuesta_sql("Cambiar registro", repuesta)

    @staticmethod
    def consultar():
        registros = operaciones.Operaciones.consultar()
        return registros

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
                messagebox.showinfo(icon="info",title=titulo,message="...¡Accion realizada con Éxito !...")
        else:
                messagebox.showinfo(icon="info",title=titulo,message="...¡No fue posible realizar la acción, vuelva a intentar por favor! ...") 