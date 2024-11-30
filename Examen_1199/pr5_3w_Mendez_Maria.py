print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
class Agenda:
    def __init__(self):        #Inicializa una lista vacía para almacenar los contactos
        self.contactos = []
    def añadir_contacto(self):        #Solicita al usuario los datos del nuevo contacto y lo añade a la lista
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el correo electrónico del contacto: ")
        contacto = {'nombre': nombre, 'telefono': telefono, 'email': email}
        self.contactos.append(contacto)
        print("Contacto añadido correctamente.")
    def lista_contactos(self):        #Muestra todos los contactos guardados en la agenda
        if self.contactos:
            print("\nLista de contactos:")
            for i, contacto in enumerate(self.contactos, start=1):
                print(f"{i}. {contacto['nombre']} - {contacto['telefono']} - {contacto['email']}")
        else:
            print("No hay contactos en la agenda.")
    def buscar_contacto(self):        #Busca un contacto por nombre y lo muestra
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre_buscar.lower():
                print(f"Contacto encontrado: {contacto['nombre']} - {contacto['telefono']} - {contacto['email']}")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")
    def editar_contacto(self):        #Permite editar un contacto por nombre
        nombre_editar = input("Ingrese el nombre del contacto a editar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre_editar.lower():
                print(f"Contacto encontrado: {contacto['nombre']} - {contacto['telefono']} - {contacto['email']}")
                contacto['nombre'] = input("Nuevo nombre: ")                 #Editar los datos que se piden o se solicitan
                contacto['telefono'] = input("Nuevo teléfono: ")
                contacto['email'] = input("Nuevo correo electrónico: ")
                print("Contacto actualizado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")
    def menu(self):        #Muestra el menú y ejecuta la opción seleccionada
        while True:
            print("\n--- Menú de la Agenda ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.lista_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                print("Cerrando la agenda...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
agenda = Agenda()          #Crear una instancia de la clase Agenda y mostrar el menú
agenda.menu()
