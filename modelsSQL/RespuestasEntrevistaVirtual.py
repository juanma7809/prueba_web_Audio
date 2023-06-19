from modelsSQL.Database import conexion


class RespuestasEntrevistaVirtual:
    def __init__(self):
        self.conexion = conexion


    def crear(self, id_entrevista, pregunta, respuesta):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO respuestas_entrevista_virtual (id_entrevista, pregunta, respuesta) VALUES (%s, %s, %s)"
            values = (id_entrevista, pregunta, respuesta,)
            cursor.execute(consulta, values)
            self.conexion.commit()
        except Exception as e:
            print(e)



    def obtener_por_id(self, id_entrevista):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM respuestas_entrevista_virtual WHERE id_entrevista = %s"
            values = (id_entrevista,)
            cursor.execute(consulta, values)
            return cursor.fetchall()
        except Exception as e:
            print(e)
    



