from tkinter import *
from tkinter import messagebox
from controller import controlador

#interfaz o view
class Vistas:
    def _init_(self,ventana):
        ventana.title("Gestion de notas")
        ventana.geometry("700x500")
        ventana.resizable(False,False) #para que la pantalla este fija
        self.interfaz(ventana)

    @staticmethod
    def interfaz(ventana):
        Vistas.borrarPantalla(ventana)
        txt_mp=Label(ventana,text="Menu Principal").pack(pady=7)
        btn1=Button(ventana,text="1.-Registro",command=lambda: Vistas.registro(ventana))
        btn1.pack(pady=7)
        btn2=Button(ventana,text="2.-Login", command=lambda: Vistas.login(ventana))
        btn2.pack(pady=7)
        btn3=Button(ventana,text="3.-Salir",command=ventana.quit)
        btn3.pack(pady=7)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def registro(ventana):
        Vistas.borrarPantalla(ventana)
        txt_re=Label(ventana,text="Registro")
        txt_re.pack(pady=7)
        lbl_n=Label(ventana,text="¿Cual es tu nombre?").pack(pady=7)
        txt_n=Entry(ventana,width=25,justify="left")
        txt_n.pack(pady=7)

        lbl_a=Label(ventana,text="¿Cuales son tus apellidos?")
        lbl_a.pack(pady=7)
        txt_a=Entry(ventana,width=25,justify="left")
        txt_a.pack(pady=7)

        lbl_e=Label(ventana,text="Ingresa tu email")
        lbl_e.pack(pady=7)
        txt_e=Entry(ventana,width=25,justify="left")
        txt_e.pack(pady=7)

        lbl_c=Label(ventana,text="Ingresa tu contraseña")
        lbl_c.pack(pady=7)
        txt_c=Entry(ventana,width=25,justify="left",show="*")
        txt_c.pack(pady=7)

        btnre=Button(ventana,text="Registrar",command=lambda: controlador.Controlador.registrar(txt_n.get(), txt_a.get(), txt_e.get(), txt_c.get())).pack(pady=7)
        btnreg = Button(ventana, text="Regresar", command=lambda: Vistas.interfaz(ventana))
        btnreg.pack()

    @staticmethod
    def login(ventana):
        Vistas.borrarPantalla(ventana)
        txt_in=Label(ventana,text="Inicio de Sesion")
        txt_in.pack(pady=7)
        lbl_em=Label(ventana,text="Ingresa tu email")
        lbl_em.pack(pady=7)
        txt_em=Entry(ventana,width=25,justify="left")
        txt_em.pack(pady=7)

        lbl_con=Label(ventana,text="Ingresa tu contraseña")
        lbl_con.pack(pady=7)
        txt_con=Entry(ventana,width=25,justify="left",show="*")
        txt_con.pack(pady=7)
        
        btnen=Button(ventana,text="Entrar",command=lambda: controlador.Controlador.login(txt_em.get(),txt_con.get(),ventana))

        btnen.pack(pady=7)
        btnregr = Button(ventana, text="Regresar", command=lambda: Vistas.interfaz(ventana))
        btnregr.pack()

    @staticmethod
    def menu_notas(ventana,usuario_id,nombre,apellidos):
        Vistas.borrarPantalla(ventana)
        global id_user,nom_user,ape_user
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos

        txt_ti=Label(ventana,text=f"Bienvenido {nombre} {apellidos} has iniciado sesion")
        txt_ti.pack(pady=7)
        btnc=Button(ventana,text="1.-Crear",command=lambda: Vistas.crear_nota(ventana))
        btnc.pack(pady=7)
        btnm=Button(ventana,text="2.-Mostrar", command=lambda: Vistas.mostrar(ventana))
        btnm.pack(pady=7)
        btncam=Button(ventana,text="3.-Cambiar",command=lambda: Vistas.cambiar_nota(ventana))
        btncam.pack(pady=7)
        btne=Button(ventana,text="4.-Eliminar", command=lambda: Vistas.borrar_nota(ventana))
        btne.pack(pady=7)
        btnv=Button(ventana,text="5.-Regresar",command=lambda: Vistas.login(ventana))
        btnv.pack(pady=7)

    @staticmethod
    def crear_nota(ventana):
        Vistas.borrarPantalla(ventana)
        lbl_cn=Label(ventana,text="Crear nota")
        lbl_cn.pack(pady=7)
        lbl_tit=Label(ventana,text="Titulo")
        lbl_tit.pack(pady=7)
        txt_tit=Entry(ventana,width=25,justify="left")
        txt_tit.pack(pady=7)

        lbl_de=Label(ventana,text="Descricpcion")
        lbl_de.pack(pady=7)
        txt_de=Entry(ventana,width=25,justify="left")
        txt_de.pack(pady=7)

        btngr=Button(ventana,text="Guardar",justify=CENTER, command=lambda: controlador.Controlador.crear_nota(id_user, txt_tit.get(), txt_de.get()))
        btngr.pack(pady=7)
        btnregre = Button(ventana, text="Volver", justify=CENTER, command=lambda: Vistas.menu_notas(ventana))
        btnregre.pack()

    @staticmethod
    def mostrar(ventana):
        Vistas.borrarPantalla(ventana)
        #txtm=Label(ventana,text=f" {nombre} {apellido} tus notas son").pack(pady=7)

        filas=""
        registros=[("1","100","Nota 1","Desc 1","2025-11-24")]
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas=filas+f"Nota: {num_notas}\nID: {fila[0]} Titulo: {fila[2]}\n  Fecha de Creacion: {fila[4]}Descripcion: {fila[3]}"
                num_notas+=1
        else:
            messagebox.showinfo(icon="info",message="No existen notas para este usuario")

        lblr=Label(ventana,text=f"{filas}")
        lblr.pack(pady=7)
        btnv=Button(ventana,text="5.-Regresar",command=lambda: Vistas.menu_notas(ventana))
        btnv.pack(pady=7)

    @staticmethod
    def cambiar_nota(ventana):
        Vistas.borrarPantalla(ventana)
        #txt=Label(ventana,text=f"{nombre} {apellido}, vamos a cambiar nota").pack(pady=7)
        lbl_id=Label(ventana,text="ID: de la nota a cambiar: ")
        lbl_id.pack(pady=7)
        txt_id=Entry(ventana,width=25,justify="left")
        txt_id.pack(pady=7)

        txt_t=Label(ventana,text="Nuevo titulo")
        txt_t.pack(pady=7)
        Entry(ventana,width=25,justify="left").pack(pady=7)
        lbl_g=Label(ventana,text="Nueva descripcion")
        lbl_g.pack(pady=7)
        txt_g=Entry(ventana,width=25,justify="left")
        txt_g.pack(pady=7)


        btng=Button(ventana,text="Guardar",command="")
        btng.pack(pady=7)
        btn2 = Button(ventana, text="Regresar", command=lambda: Vistas.menu_notas(ventana))
        btn2.pack()

    @staticmethod
    def borrar_nota(ventana):
        Vistas.borrarPantalla(ventana)
        #txt=Label(ventana,text=f"{nombre} {apellido}, vamos a cambiar nota").pack(pady=7)
        lbl_id=Label(ventana,text="ID: de la nota a eliminar: ")
        lbl_id.pack(pady=7)
        txt_id=Entry(ventana,width=25,justify="left")
        txt_id.pack(pady=7)

        btng=Button(ventana,text="Eliminar",command="")
        btng.pack(pady=7)
        btn2 = Button(ventana, text="Regresar", command=lambda: Vistas.menu_notas(ventana))
        btn2.pack()
