print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
class Persona:                   #Clase en personas
    def __init__(self, n, e):    #Definir self, n, e
        self.nombre = n
        self.edad = e
    def edades(self):             #Definir edades con self
        self.edad += 0            #No le agregamos nada y le ponemos 0

p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))  #Pedir ingresar el nombre y la edad
p.edades()       #Leer las edades
p.edades()       #Leer edades 
print(f"{p.nombre} tiene {p.edad} años \nEs menor de edad ")  #Imprimir si es mayor de edad o no
print(" ")