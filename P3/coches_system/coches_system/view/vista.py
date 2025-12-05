from tkinter import *
from controller.controlador import Controlador
class Vistas:
    @staticmethod
    def borrarPantalla(ventana):
        for w in ventana.winfo_children(): w.destroy()
    
    @staticmethod
    def interfaz(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana ,text="Menu Principal").pack(pady=5)
        Button(ventana,text="Autos",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)
        Button(ventana,text="Camionetas",width=20,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Camiones",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Salir",width=20,command=ventana.quit).pack(pady=5)
    
    @staticmethod
    def menu_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Menú Autos").pack(pady=5)
        Button(ventana,text="Insertar",width=20,command=lambda:Vistas.insertar_autos(ventana)).pack(pady=5)
        Button(ventana,text="Consultar",width=20,command=lambda:Vistas.consultar_autos(ventana)).pack(pady=5)
        Button(ventana,text="Modificar",width=20,command=lambda:Vistas.modificar_autos(ventana)).pack(pady=5)
        Button(ventana,text="Eliminar",width=20,command=lambda:Vistas.eliminar_autos(ventana)).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.interfaz(ventana)).pack(pady=5)
   
    @staticmethod
    def insertar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Insertar Auto").pack(pady=5)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas"]; ents=[]
        for t in lbl:
            Label(ventana,text=t).pack(); e=Entry(ventana); e.pack(); ents.append(e)
        Button(ventana,text="Guardar",width=20,command=lambda:Controlador.insertar_auto(*[e.get() for e in ents])).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)
    
    @staticmethod
    def consultar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Autos Registrados").pack(pady=5)
        datos=Controlador.consultar_auto("all")
        if not datos:
            Label(ventana,text="No hay autos registrados").pack(pady=5)
        else:
            for a in datos:
                Label(ventana,text=f"id {a[0]} {a[1]}  {a[2]} {a[3]} {a[4]} {a[5]} {a[6]}").pack()
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)
    
    @staticmethod
    def modificar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Modificar Auto").pack(pady=5)
        Label(ventana,text="ID").pack(); e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",width=20,command=lambda:Vistas.modificar_form(ventana,e.get())).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)
    
    @staticmethod
    def modificar_form(ventana,id):
        auto=Controlador.consultar_auto(id)
        if not auto:
            Vistas.borrarPantalla(ventana)
            Label(ventana,text="No existe ese ID").pack(pady=5)
            Button(ventana,text="Regresar",width=20,command=lambda: Vistas.modificar_autos(ventana)).pack(pady=5)
            return
        if isinstance(auto,list) and len(auto)>0: auto=auto[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"Modificar Auto id {id}").pack(pady=5)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas"]; ents=[]
        for i,t in enumerate(lbl):
            Label(ventana,text=t).pack(); e=Entry(ventana); e.insert(0,str(auto[i+1])); e.pack(); ents.append(e)
        Button(ventana,text="Guardar Cambios",width=20,command=lambda: Controlador.modificar_auto(*[e.get() for e in ents],id)).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda: Vistas.menu_autos(ventana)).pack(pady=5)

    @staticmethod
    def eliminar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Eliminar Auto").pack(pady=5)
        Label(ventana,text="ID").pack(); e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",width=20,command=lambda:Vistas.eliminar_confirmar(ventana,e.get())).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)

    @staticmethod
    def eliminar_confirmar(ventana,id):
        auto=Controlador.consultar_auto(id)
        if not auto:
            Vistas.borrarPantalla(ventana); Label(ventana,text="No existe ese ID").pack(pady=5)
            Button(ventana,text="Regresar",width=20,command=lambda:Vistas.eliminar_autos(ventana)).pack(pady=5); return
        auto=auto[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"¿Eliminar auto? id {auto[0]} {auto[1]} {auto[2]} {auto[3]}").pack(pady=10)
        Button(ventana,text="Sí",width=20,command=lambda:Controlador.eliminar_auto(id)).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)


  #camionetas
    @staticmethod
    def menu_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Menú Camionetas").pack(pady=5)
        Button(ventana,text="Insertar",width=20,command=lambda:Vistas.insertar_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Consultar",width=20,command=lambda:Vistas.consultar_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Modificar",width=20,command=lambda:Vistas.modificar_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Eliminar",width=20,command=lambda:Vistas.eliminar_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.interfaz(ventana)).pack(pady=5)

    def insertar_camionetas(ventana):
        vistas.borrarPantalla(ventana)
        Label(ventana,text="Insertar Camioneta").pack(pady=5)
        txt_marca=Label(ventana,text="Marca");txt_marca.pack(); e_marca=Entry(ventana); e_marca.pack()
        txt_color=Label(ventana,text="Color"); txt_color.pack(); e_color=Entry(ventana); e_color.pack()
        txt_modelo=Label(ventana,text="Modelo"); txt_modelo.pack(); e_modelo=Entry(ventana); e_modelo.pack()
        txt_velocidad=Label(ventana,text="Velocidad"); txt_velocidad.pack(); e_velocidad=Entry(ventana); e_velocidad.pack()
        txt_caballaje=Label(ventana,text="Caballaje"); txt_caballaje.pack(); e_caballaje=Entry(ventana); e_caballaje.pack()
        txt_plazas=Label(ventana,text="Plazas"); txt_plazas.pack(); e_plazas=Entry(ventana); e_plazas.pack()
        txt_traccion=Label(ventana,text="Tracción"); txt_traccion.pack(); e_traccion=Entry(ventana); e_traccion.pack()

        Button(ventana,text="Guardar",width=20,command=lambda:"").pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=5)

    def consultar_camionetas(ventana):
        vistas.borrarPantalla(ventana)
        txt_titulo=Label(ventana,text="Consultar Camionetas"); txt_titulo.pack(pady=5)
        
        btn_regresar=Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camionetas(ventana)); btn_regresar.pack(pady=5)

    def modificar_camionetas(ventana):
        vistas.borrarPantalla(ventana)
        txt_titulo=Label(ventana,text="Modificar Camioneta"); txt_titulo.pack(pady=5)
        
        btn_regresar=Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camionetas(ventana)); btn_regresar.pack(pady=5)

    def eliminar_camionetas(ventana):
        vistas.borrarPantalla(ventana)
        txt_titulo=Label(ventana,text="Eliminar Camioneta"); txt_titulo.pack(pady=5)
        
        btn_regresar=Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camionetas(ventana)); btn_regresar.pack(pady=5)

    #camiones
    @staticmethod
    def menu_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Menú Camiones").pack(pady=5)
        Button(ventana,text="Insertar",width=20,command=lambda:Vistas.insertar_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Consultar",width=20,command=lambda:Vistas.consultar_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Modificar",width=20,command=lambda:Vistas.modificar_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Eliminar",width=20,command=lambda:Vistas.eliminar_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.interfaz(ventana)).pack(pady=5)

    @staticmethod
    def insertar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Insertar Camión").pack(pady=5)
        lbls=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas","Carga"]
        ents=[]
        for t in lbls:
            Label(ventana,text=t).pack(); e=Entry(ventana); e.pack(); ents.append(e)
        Button(ventana,text="Guardar",width=20,command=lambda:None).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)

    @staticmethod
    def consultar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Consultar Camiones").pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)

    @staticmethod
    def modificar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Modificar Camión").pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)

    @staticmethod
    def eliminar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Eliminar Camión").pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)
