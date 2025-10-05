#Instalar los objetos para posteriormente implementarlos
from coches import coches,Camionetas,Camiones
import os
os.system("cls")

def borrarPantalla():
  os.system("cls")

def esperarTecla():
  input("\n\t ...Oprima una tecla para continuar...")

def datos_autos(tipo):
  borrarPantalla()
  print(f"\n\t ...Ingresar los datos del vehiculo de tipo {tipo}...")
  marca=input("Marca: ") .upper
  color=input("Color: ") .upper
  modelo=input("Modelo: ") .upper
  velocidad=int(input("Velocidad: "))
  potencia=int(input("Potencia: "))
  plazas=int(input("Numero de plazas: "))
  return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,caballaje,plazas):
  print(f"Datos del vehiculo: \n Marca: {marca} \n Color: {color} \n Modelo: {modelo} \n Velocidad: {velocidad} \n Caballaje: {caballaje} \n Plazas: {plazas}")
 
def autos():
  marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
  coche=coches(marca,color,modelo,velocidad,potencia,plazas)
  imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)

def camiones():
  marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
  eje=int(input("Número de ejes: "))
  capacidadCarga=int(input("Capacidad de carga: "))
  coche=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
  imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
  print(f"\n Ejes: {coche.ejes} \n Capacidad de Carga: {coche.capacidadCarga}")

def camionetas():
  marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camionetas")
  traccion=(input("Traccion: "))  .upper
  cerrada=(input("Cerrada (SI/NO)")).upper .strip
  if cerrada =="SI":
    cerrada=True
  else: 
    cerrada=False
  coche=Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
  imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
  print(f"\n traccion: {coche.traccion} \n Cerrada: {coche.cerrada}")

def main():
 opcion=True
 while opcion:
  opcion=input("\n\t\t ...Menu Principal... \n1. Autos\n2. Camionetas\n3. Camiones\n4. Salir\n\tElige una opcion: ").lower() .strip()
 match opcion:
    case "1":
     autos()
     esperarTecla()
    case "2":
     camionetas()
     esperarTecla()
    case "3":
     camiones()
     esperarTecla()
    case "4":
        borrarPantalla()
        print("Gracias por utilizar el SW")
        input("Salir del sistema")
        opcion=False
    case _:
      input("Opcion no valida   vuelva a intentarlo")

if __name__=="__main__":
  main()
