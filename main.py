from data_persistence.database import Database
from config.db_config import mydb
import utils.format_data as format_data

new_db = Database(mydb)

def menuPrincipal():
    aContinuar = True
    while(aContinuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("########################### MENÚ ###########################")
            print("1.- Traer Leyes")
            print("2.- Traer Ley por N° de Registro")
            print("3.- Traer Ley por palabra clave")
            print("4.- Registrar Ley")
            print("5.- Actualizar Ley")
            print("6.- Borrar Ley")
            print("7.- Salir")
            print("#############################################################")

            opcion = int(input("Elegir una opción: "))

            if opcion < 1 or opcion > 7:
                print("Incorrect choice. Choose a different one")
            elif opcion == 7:
                aContinuar = False
                print("¡Gracias por utilizar nuestros servicios!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    if opcion == 1:
        try:
            leyes = new_db.get_all_laws()
            if len(leyes) > 0:
                format_data.format_data(leyes)
            else:
                print("No hay Leyes")
        except:
             print("Hubo un error")
    elif opcion == 2:
       print("Hubo un error")
    elif opcion == 3:
        print("Hubo un error")
    elif opcion == 4:
        print("Registrar Leyes")
    elif opcion == 5:
        print("Actualizar Ley")
    elif opcion == 6:
        print("Borrar Ley")
    else:
        print("¡Lo sentimos, vuelva a intentarlo!")

menuPrincipal()