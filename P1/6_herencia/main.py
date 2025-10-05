#Instalar los objetos para posteriormente implementarlos
import os
os.system("cls")

#Instanciar los objetos para posteriormente implementarlos 

from coches import Coches, Camionetas, Camiones

coche=Coches("VW","Blanco","2020",220,200,5)
print(coche.marca, coche.acelerar())

camioneta=Camionetas("Nissan","Amarillo","2025",180,200,4,"trasera",False)
print(camioneta.marca, coche.acelerar())





"""
num_coches=int(input("Cuantos coches deseas?"))

for i in range(0, num_coches):
 print(f"\n\t ...Datos del coche {i+1}... \n")
 marca=input("Ingresa la marca: ") .upper
 color=input("Ingresa el color: ") .upper
 modelo=input("Ingresa el modelo: ") .upper
 velocidad=int(input("Ingresa la velocidad: "))
 potencia=int(input("Ingresa la potencia: "))
 plazas=int(input("Ingresa las plazas: "))

 coche1=coches(marca,color,modelo,velocidad,potencia,plazas)
 
 print(f"Datos del vehiculo: \n Marca: {coche1.getMarca()} \n Color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n Velocidad: {coche1.getVelocidad()} \n Caballaje: {coche1.getCaballaje()} \n Plazas: {coche1.getPlazas()}")
 print(f"\n\t {coche1.acelerar()}")

#segunda manera
import coches
coches=coches.coches("VW","Blanco","2022",220,150,5)
"""
