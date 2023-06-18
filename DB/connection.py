import mysql.connector
from mysql.connector import Error  

#Data Access Object
class DAO():
 
    def __init__(self): 
        try:
            self.connect = mysql.connector.connect(
                host ='bcoaayn1yza5y2d8potc-mysql.services.clever-cloud.com',
                port = 3306,
                user = 'uhdijdgl8byqc9qr',
                password = 'ExBnDdB88xdyssCQYLtT',
                db= "bcoaayn1yza5y2d8potc"
            
    )

        except Error as ex:
            print(ex)


    def traerLeyes(self):
        if self.connect.is_connected():
            try:
                cursor = self.connect.cursor()
                cursor.execute("SELECT leyes.nro_registro, leyes.nro_normativa, leyes.fecha, leyes.palabras_clave, leyes.descripcion, tipos_normativa.tipo_normativa, categorias.categoria, jurisdicciones.jurisdiccion, organos_legislativos.organo_legislativo FROM leyes JOIN tipos_normativa ON leyes.tipos_normativa_id_tipo_normativa = tipos_normativa.id_tipo_normativa JOIN categorias ON leyes.categorias_id_categoria = categorias.id_categoria JOIN jurisdicciones ON leyes.jurisdicciones_id_jurisdiccion = jurisdicciones.id_jurisdiccion JOIN organos_legislativos ON leyes.organos_legislativos_id_organo_legislativo = organos_legislativos.id_organo_legislativo")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(ex)