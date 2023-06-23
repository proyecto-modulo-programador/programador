class Menu:
    def __init__(self, database):
        self.database = database

    def show_menu(self):
        print("########################### MENÚ ###########################")
        print("1.- Traer Leyes")
        print("2.- Traer Ley por N° de Ley")
        print("3.- Traer Ley por palabra clave")
        print("4.- Registrar Ley")
        print("5.- Actualizar Ley")
        print("6.- Borrar Ley")
        print("7.- Salir")
        print("#############################################################")

    def get_laws(self):
        self.database.get_all_laws()

    def get_law_by_num(self, law_num):
        self.database.get_law_by_num(law_num)

    def get_law_by_keyword(self, keyword):
        self.database.get_law_by_keyword(keyword) 

    def register_law(self):
        normative_type = input('Selecciona el n° correspondiente al tipo de normativa:\n1) Ley\n2) Decreto\n3) Resolución\n')
        normative_num = input('Ingresa el número de la normativa: ')
        date = input('Ingresa la fecha en formato AAAA-MM-DD: ')
        description = input('Ingresa una breve descripción: ')
        category = input('Selecciona el n° correspondiente a la categoría:\n1) Laboral\n2) Penal\n3) Civil\n4) Comercial\n5) Familia y sucesiones\n6) Agrario y ambiental\n7) Minería\n8) Derecho informático\n')
        jurisdiction = input('Selecciona el n° correspondiente a la jurisdicción:\n1) Nacional\n2) Provincial\n')
        keywords = input('Ingresa las palabras clave separadas por coma: ')
        print(self.database.add_law(normative_num, date, keywords, description, category, jurisdiction, normative_type))

    def update_law(self):
        register_num = input('Ingresa el número de registro de la ley: ')
        description = input('Ingresa la nueva descripción: ')
        print(self.database.update_law_by_register_num(register_num, description))

    def delete_law(self):
        register_num = input('Ingresa el número de registro de la ley: ')
        print(self.database.delete_law_by_register_num(register_num))

    def run(self):
        while True:
            self.show_menu()
            option = input("Elegir una opción: ")

            if option == '1':
                self.get_laws()
            elif option == '2':
                law_num = input('Ingresa el número de la ley: ')
                self.get_law_by_num(law_num)
            elif option == '3':
                keyword = input('Ingresa la palabra clave: ')
                self.get_law_by_keyword(keyword)
            elif option == '4':
                self.register_law()
            elif option == '5':
                self.update_law()
            elif option == '6':
                self.delete_law()
            elif option == '7':
                print('¡Gracias por utilizar nuestros servicios!')
                break
            else:
                print('Opción no válida ¡Vuelva a intentarlo!') 