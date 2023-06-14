from modelsSQL.Database import conexion

class PacienteVideo:
    def __init__(self):
        self.conexion = conexion

    def crear(self, id_paciente, id_video, diagnostico):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO paciente_video (id_paciente, id_video, diagnostico) VALUES (%s, %s, %s)"
            valores = (id_paciente, id_video, diagnostico)
            cursor.execute(consulta, valores)
            self.conexion.commit()
            cursor.close()
        except Exception as e:
            print(e)


    def obtener_por_id_paciente(self, id_paciente):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM paciente_video WHERE id_paciente = %s"
            valores = (id_paciente,)
            cursor.execute(consulta, valores)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)
    
    def obtener_videos_por_id_paciente(self, id_paciente):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT id_video FROM paciente_video WHERE id_paciente = %s"
            valores = (id_paciente,)
            cursor.execute(consulta, valores)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)