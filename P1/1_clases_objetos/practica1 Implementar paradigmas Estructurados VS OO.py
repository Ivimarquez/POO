"""
Practica#1 implementar paradigma estructurado VS OO 
Crear un progrma que obtenga el area y perimetro de un rectangulo
"""

import os
os.system("cls")
#1 Estructurado


def areaRectangulo(base, altura):
    area=base*altura
    return area

base = 5
altura = 6
print(f"El area del rectangulo es: {areaRectangulo(base, altura)}")


#2 OO
class AreaRectangulo:
    def __init__(self, base, altura):
       self.base=base
       self.altura=altura
    def areaRectangulo(self):
     area=self.base*self.altura
     return area
    
rectagulo=AreaRectangulo(5,6) #instanciar un objeto de la clase AreaRectangulo
print(f"El area del rectangulo es: {rectagulo.areaRectangulo(base, altura)}")