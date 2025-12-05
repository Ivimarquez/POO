from model.cochesBD import Autos
from tkinter import messagebox
class Controlador:
    @staticmethod
    def insertar_auto(marca,color,modelo,velocidad,caballaje,plazas):
        r=Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas); Controlador.respuesta_sql("Insertar Auto",r)
    @staticmethod
    def consultar_auto(id):
        if id=="all": return Autos.consultar()
        else: return Autos.consultarID(id)
    @staticmethod
    def modificar_auto(marca,color,modelo,velocidad,caballaje,plazas,id):
        r=Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id); Controlador.respuesta_sql("Modificar Auto",r)
    @staticmethod
    def eliminar_auto(id):
        r=Autos.eliminar(id); Controlador.respuesta_sql("Eliminar Auto",r)
    @staticmethod
    def respuesta_sql(t,res):
        if res: messagebox.showinfo(t,"Acción realizada con éxito")
        else: messagebox.showerror(t,"No se pudo completar la acción")
