from modelsSQL.Database import conexion


class EntrevistaVirtual:
    def __init__(self):
        self.conexion = conexion


    def crear(self, id):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO entrevista_virtual (id_paciente) VALUES (%s)"
            values = (id,)
            cursor.execute(consulta, values)
            self.conexion.commit()
            consulta =  "SELECT LAST_INSERT_ID()"
            cursor.execute(consulta)
            resultado = cursor.fetchone()
            return resultado[0]
        except Exception as e:
            print(e)



    def obtener_por_id_paciente(self, id_paciente):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM entrevista_virtual WHERE id_paciente = %s"
            values = (id_paciente,)
            cursor.execute(consulta, values)
            return cursor.fetchall()
        except Exception as e:
            print(e)
    



