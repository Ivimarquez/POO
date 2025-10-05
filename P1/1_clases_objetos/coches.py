import os
os.system("cls")

class coches:
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas

    def acelerar(self,incremento):
        self.__velocidad=self.__velocidad+incremento
        self.__caballaje=self.__caballaje+incremento
        return self.__velocidad

    def frenar(self,decremento):
        self.__velocidad=self.__velocidad-decremento
        self.__caballaje=self.__caballaje-decremento
        return self.__velocidad
    

coche1=coches("VM", "Blanco", 2022, 220, 150,5)
coche2=coches("Nissan", "Azul", 2020, 180,150, 6)

print(f"Los valores del objeto 1 son: {coche1.__marca}, {coche1.__color}, {coche1.__modelo}, {coche1.__velocidad}, {coche1.__caballaje}, {coche1.__plazas}")




marca=""
color=""
modelo=""
velocidad=0
caballaje=0 
plazas=0

def acelerar():
    pass

def frenar():
    pass

coche1=coches()
coche1.marca="VM"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

print(f"Datos del vehiculo: \n Marca: {coche1.marca} \n Color: {coche1.color} \n Modelo: {coche1.modelo} \n Velocidad: {coche1.velocidad} \n Caballaje: {coche1.caballaje} \n Plazas: {coche1.plazas}")

coche2=coches()
coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(f"Datos del vehiculo: \n Marca: {coche2.marca} \n Color: {coche2.color} \n Modelo: {coche2.modelo} \n Velocidad: {coche2.velocidad} \n Caballaje: {coche2.caballaje} \n Plazas: {coche2.plazas}")
