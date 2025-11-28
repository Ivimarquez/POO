from tkinter import *
from controller import funciones
from model import operaciones
from tkinter import messagebox

#interfaz o view
class Vistas:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("600x400")
        ventana.resizable(False,False) #para que la pantalla este fija
        self.interfaz(ventana)
    
    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana,textvariable=n1, width=5,justify="right")
        txt_numero1.pack(side="top", anchor="center",pady=10)
        txt_numero2=Entry(ventana,textvariable=n2, width=5,justify="right")
        txt_numero2.pack(side="top", anchor="center",pady=10)

        btn_sum=Button(ventana,text="+",command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        btn_sum.pack(pady=5)
        btn_resta=Button(ventana,text="-", command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        btn_resta.pack(pady=5)
        btn_multi=Button(ventana, text="*", command=lambda: funciones.Controladores.operaciones("Multiplicacion",n1.get(),n2.get(),"x"))
        btn_multi.pack(pady=5)
        btn_division=Button(ventana,text="/",command=lambda: funciones.Controladores.operaciones("Division",n1.get(),n2.get(),"/"))
        btn_division.pack(pady=5)
        btn_salir=Button(ventana,text="Salir", command=ventana.quit)
        btn_salir.pack(pady=10)

    def menuPrincipal(self,ventana):
        menubar=Menu(ventana)  
        ventana.config(menu=menubar)
        archivoMenu=Menu(menubar,tearoff=False)
        menubar.add_cascade(label="Operaciones",menu=archivoMenu)
        archivoMenu.add_command(label="Agregar",command=lambda: self.interfaz(ventana))
        archivoMenu.add_command(label="Consultar",command=lambda: self.consultar(ventana))
        archivoMenu.add_command(label="Cambiar",command=lambda: self.cambiar(ventana))
        archivoMenu.add_command(label="Borrar",command=lambda: self.borrar(ventana))
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir",command=ventana.quit)

    def borrar(self,ventana):
        self.menuPrincipal(ventana)
        eti1=Label(ventana,text="Borrar una Operacion")
        eti1.pack(pady=8)
        eti2=Label(ventana,text="ID de la Operacion: ")
        eti2.pack(pady=8)
        id=IntVar()
        txt_ope=Entry(ventana,textvariable=id,justify="right",width=5)
        txt_ope.pack()
        btn=Button(ventana,text=("Eliminar"),command="")
        btn.pack()
        eti0=Label(ventana,text="Operacion borrada con exito")
        eti0.pack(pady=8)
        btn2=Button(ventana,text=("Volver"),command= self.interfaz(ventana))
        btn2.pack()
        self.borrarPantalla(ventana)
        self.menu(ventana)
        eti1=Label(ventana,text="Borrar una Operacion")
        eti1.pack(pady=8)
        eti2=Label(ventana,text="ID de la Operacion: ")
        eti2.pack(pady=8)
        oper_id=IntVar()
        txt_ope=Entry(ventana,textvariable=oper_id,justify="right",width=5)
        txt_ope.pack()
        btn=Button(ventana,text="Eliminar",command=lambda: None)
        btn.pack()
        btn2=Button(ventana,text="Volver",command=lambda: self.interfaz(ventana))
        btn2.pack()
    
    def borrarPantalla(self, ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def consultar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        eti1=Label(ventana,text="Listado de las Operaciones")
        eti1.pack(pady=10)
       
        registros=operaciones.Operaciones.consultar()
        filas=""
        if len(registros)>0:
            num_operaciones=1
            for fila in registros:
                filas=filas+f"\nOperacion:{num_operaciones} ID:{fila[0]} Fecha de creacion:{fila[1]}\nOperacion:{fila[2]} {fila[4]} {fila[3]}={fila[5]}"
                num_operaciones+=1
        else:   
            messagebox.showinfo(icon="info",message="No existen operaciones en el sistema..agrega operaciones..")

    def cambiar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        eti1=Label(ventana,text=f"Cambiar una Operacion")
        eti1.pack(pady=8)
        eti2=Label(ventana,text="ID de la Operacion: ")
        eti2.pack(pady=8)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=5)
        txt_id.pack()
        eti3=Label(ventana,text="Nuevo numero 1: ")
        eti3.pack(pady=8)
        num1=IntVar()
        txt_num1=Entry(ventana,textvariable=num1,justify="right",width=5)
        txt_num1.pack()
        eti4=Label(ventana,text="Nuevo numero 2: ")
        eti4.pack(pady=8)
        num2=IntVar()
        txt_num2=Entry(ventana,textvariable=num2,justify="right",width=5)
        txt_num2.pack()
        eti5=Label(ventana,text="Nuevo signo: ")
        eti5.pack(pady=8)
        signo=StringVar()
        txt_signo=Entry(ventana,textvariable=signo,justify="right",width=5)
        txt_signo.pack()
        eti5=Label(ventana,text="Nuevo resultado: ")
        eti5.pack(pady=8)
        resultado=DoubleVar()
        txt_resultado=Entry(ventana,textvariable=resultado,justify="right",width=5)
        txt_resultado.pack()

        btn=Button(ventana,justify="right",width=5,text=("Guardar"),command=lambda:funciones.Controladores.cambiar(
            num1.get(),num2.get(),signo.get(),resultado.get(),id.get()))
        btn.pack()
        btn2=Button(ventana,justify="right",width=5,text=("Volver"),command=lambda: self.interfaz(ventana))
        btn2.pack()