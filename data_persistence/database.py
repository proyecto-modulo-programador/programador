from mysql.connector import Error
import utils.format_data as format_data

class Database():

    def __init__(self, db):
        self.db = db
        self.mycursor = db.cursor()

    def get_all_laws(self):
        try:
            self.mycursor.execute("SELECT leyes.nro_registro, leyes.nro_normativa, leyes.fecha, leyes.palabras_clave, leyes.descripcion, tipos_normativa.tipo_normativa, categorias.categoria, jurisdicciones.jurisdiccion, organos_legislativos.organo_legislativo FROM leyes JOIN tipos_normativa ON leyes.tipos_normativa_id_tipo_normativa = tipos_normativa.id_tipo_normativa JOIN categorias ON leyes.categorias_id_categoria = categorias.id_categoria JOIN jurisdicciones ON leyes.jurisdicciones_id_jurisdiccion = jurisdicciones.id_jurisdiccion JOIN organos_legislativos ON leyes.organos_legislativos_id_organo_legislativo = organos_legislativos.id_organo_legislativo")
            result = self.mycursor.fetchall()
            if len(result) > 0:
                return format_data.format_data(result)
            else:
                print("No hay leyes")
        except Error:
            print(f"Hubo un error, {Error}")

    def get_law_by_num(self, lawNum):
        try:
            self.mycursor.execute(
                f"SELECT leyes.nro_registro, leyes.nro_normativa, leyes.fecha, leyes.palabras_clave, leyes.descripcion, tipos_normativa.tipo_normativa, categorias.categoria, jurisdicciones.jurisdiccion, organos_legislativos.organo_legislativo FROM leyes JOIN tipos_normativa ON leyes.tipos_normativa_id_tipo_normativa = tipos_normativa.id_tipo_normativa JOIN categorias ON leyes.categorias_id_categoria = categorias.id_categoria JOIN jurisdicciones ON leyes.jurisdicciones_id_jurisdiccion = jurisdicciones.id_jurisdiccion JOIN organos_legislativos ON leyes.organos_legislativos_id_organo_legislativo = organos_legislativos.id_organo_legislativo WHERE leyes.nro_normativa = {lawNum}")

            myresult = self.mycursor.fetchall()
            if len(myresult) > 0:
                return format_data.format_data(myresult)
            else:
                print("No hay leyes")
        except Error:
            print(f"Hubo un error, {Error}")

    def get_law_by_keyword(self, keyword):
        try:
            self.mycursor.execute(
                f"SELECT leyes.nro_registro, leyes.nro_normativa, leyes.fecha, leyes.palabras_clave, leyes.descripcion, tipos_normativa.tipo_normativa, categorias.categoria, jurisdicciones.jurisdiccion, organos_legislativos.organo_legislativo FROM leyes JOIN tipos_normativa ON leyes.tipos_normativa_id_tipo_normativa = tipos_normativa.id_tipo_normativa JOIN categorias ON leyes.categorias_id_categoria = categorias.id_categoria JOIN jurisdicciones ON leyes.jurisdicciones_id_jurisdiccion = jurisdicciones.id_jurisdiccion JOIN organos_legislativos ON leyes.organos_legislativos_id_organo_legislativo = organos_legislativos.id_organo_legislativo WHERE leyes.palabras_clave LIKE '%{keyword}%'")

            myresult = self.mycursor.fetchall()
            if len(myresult) > 0:
                return format_data.format_data(myresult)
            else:
                print("No hay leyes")
        except Error:
            print(f"Hubo un error, {Error}")

    def add_law(self, normative_num, date, keywords, description, category, jurisdiction, normative_type):
        try:
            # Esta validación es debido a que Si la ley es nacional, el órgano legislativo es el Congreso de la Nación; si la ley es provincial, el órgano legislativo es la Legislatura de Córdoba. Como en la DB tienen el mismo número de id, se puede usar la misma variable.
            legislative_organ = jurisdiction

            sql = "INSERT INTO leyes (nro_normativa, fecha, palabras_clave, descripcion, categorias_id_categoria, jurisdicciones_id_jurisdiccion, organos_legislativos_id_organo_legislativo, tipos_normativa_id_tipo_normativa) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s, %s)"
            val = (normative_num, date, keywords, description, category,
                   jurisdiction, legislative_organ, normative_type)

            self.mycursor.execute(sql, val)
            self.db.commit()
            return 'Ley agregada correctamente'
        except Error:
            return f"Hubo un error, {Error}" 

    def update_law_by_register_num(self, register_num, description):
        try:
            self.mycursor.execute(
                f"UPDATE leyes SET descripcion = '{description}' WHERE nro_registro = {register_num}")
            self.db.commit()
            return 'Ley actualizada correctamente'
        except Error:
            return f"Hubo un error, {Error}"

    def delete_law_by_register_num(self, register_num):
        try:
            self.mycursor.execute(
                f"DELETE FROM leyes WHERE nro_registro = {register_num}")
            self.db.commit()
            return 'Ley eliminada correctamente'
        except Error:
            return f"Hubo un error, {Error}" 