print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
class Estudiante():                        #Clase con estudiantes
    def __init__(self, nombre, nota):      #Definir self, nombre y nota
        self.nombre = nombre               
        self.nota = nota
    def imprimir(self):                    #Definir para imprimir self
        print(f"Nombre: {self.nombre}\nNota: {self.nota}")  #Imprimir el nombre y la nota
    def resultados(self):                         #Hacer que funcione el codigo con self
        if self.nota >= 7:                        #Si sla nota es mayopr o igual a 7
            print("¡Has APROBADO!")               #Imprime estas aprovado
        else:                                     #Si no 
            print("Has REPROBADO!")               #Estas reprovado
estudiante1 = Estudiante("Maria", 10)             #La estudiante es maria y saco 10
estudiante1.imprimir()                            #Imprimir
estudiante1.resultados()                          #Imprir si esta aprovada en base a lo dado
print(" ")