

#class Calculadora:
    #def __init__  
    #num1=int(input("Ingrese el primer numero: "))
    #num2=int(input("Ingrese el segundo numero: "))

    #def suma: 
    #suma=num1+num2
    #print(f"El resultado de la suma es: {suma}")

    #def resta:
    #resta=num1-num2
    #print(f"El resultado de la resta es: {resta}")

    #def multiplicacion:
    #multi=num1*num2
    #print(f"El resultado de la multiplicacion es: {multi}")

    #def division:
    #divi=num1/num2
    #print(f"El resultado de la division es: {divi}")




class Calculadora:
    def __init__(self):
        self._numero1=int(input("Numero #1: "))
        self._numero2=int(input("Numero #2: "))

    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self,numero1):
        self._numero1=numero1

    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self,numero2):
        self._numero2=numero2

    def sumar(self):
        return self._numero1 + self._numero2
    
    def restar(self):
        return self._numero1 - self._numero2
    
    def multiplicar(self):
        return self._numero1 * self._numero2

    def dividir(self):
        return self._numero1 / self._numero2
    
operacion=Calculadora()
print(f"operacion.sumar(): ")
print(f"{operacion.numero1} + {operacion.numero2} = {operacion.sumar()}")
print(f"{operacion.numero1} - {operacion.numero2} = {operacion.restar()}")
print(f"{operacion.numero1} * {operacion.numero2} = {operacion.multiplicar()}")
print(f"{operacion.numero1} / {operacion.numero2} = {operacion.dividir()}")