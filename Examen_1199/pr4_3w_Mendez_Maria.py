print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
class Calculadora:                        #Calculadora
    def __init__(self, num1, num2):       #DEfinir self, numero1 y numero2
        self._num1 = num1                 
        self._num2 = num2
    def suma(self):                       #Definir suma como self
        resultado = self._num1 + self._num2     #Resultado es igual a selnum1 y selfnum2
        #Imprimir el resultado de la suma
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")
    def resta(self):
        resultado = self._num1 - self._num2
        #Imprimir el resultado de la resta en base a lo dicho
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")
    def division(self):
        if self._num2 != 0:
            resultado = self._num1 / self._num2
        #Imprimir el resultado de la division en base a lo dicho
            print(f"El resultado de la división es: {self._num1} / {self._num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre 0")
    def multiplicacion(self):
        resultado = self._num1 * self._num2
        #Imprimir el resultado de la multilicacion en base a lo dicho
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")
#Algunas operaciones a hyacer en base a lo dicho
operacion = Calculadora(20, 5)    #Calcular 20+5
operacion.suma() #Hacer suma
operacion = Calculadora(100, 2)   #Calcular 100-2
operacion.resta() #Hacer resta
operacion = Calculadora(50, 6)    #Calcular 50/6
operacion.division()  #Hacer division
operacion = Calculadora(70, 1)    #Calcular 70*1
operacion.multiplicacion() #Hacer multiplicacion
print(" ")