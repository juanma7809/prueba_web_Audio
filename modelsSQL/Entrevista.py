from modelsSQL.Database import conexion

class Entrevista:
    def __init__(self):
        self.conexion = conexion
    
    def crear(self, id_entrevistador, diagnostico, id_paciente):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO entrevista (id_entrevistador, diagnostico, id_paciente) VALUES (%s, %s, %s)"
            valores = (id_entrevistador, diagnostico, id_paciente,)
            cursor.execute(consulta, valores)
            self.conexion.commit()
        except Exception as e:
            print(e)
    
    def obtener_por_id_paciente(self, id_paciente):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM entrevista WHERE id_paciente = %s"
            values = (id_paciente,)
            cursor.execute(consulta, values)
            return cursor.fetchall()
        except Exception as e:
            print(e)
    
  