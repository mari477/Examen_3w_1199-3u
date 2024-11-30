print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
#Inicializa los atributos del triángulo
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def lado_mayor(self):
#Devuelve el valor del lado con mayor tamaño
        mayor = max(self.lado1, self.lado2, self.lado3)
        return mayor
    def tipo_triangulo(self):
#Determina el tipo de triángulo
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    def imprimir_informacion(self):
#Imprime el valor del lado mayor y el tipo de triángulo
        print(f"Lado mayor: {self.lado_mayor()}")
        print(f"Tipo de triángulo: {self.tipo_triangulo()}")
if __name__ == "__main__":
#Solicitar los datos al usuario
    lado1 = float(input("Ingresa el valor del primer lado: "))
    lado2 = float(input("Ingresa el valor del segundo lado: "))
    lado3 = float(input("Ingresa el valor del tercer lado: "))
#Crear una instancia de la clase Triangulo
    triangulo = Triangulo(lado1, lado2, lado3)
#Imprimir la información sobre el triángulo
    triangulo.imprimir_informacion()
print(" ")
