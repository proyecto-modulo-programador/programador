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