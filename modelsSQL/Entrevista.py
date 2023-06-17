from modelsSQL.Database import conexion

class Entrevista:
    def __init__(self):
        self.conexion = conexion
    
    def crear(self, id_entrevistador, diagnostico, id_paciente, diagnostico_depresion):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO entrevista (id_entrevistador, diagnostico, id_paciente, diagnostico_depresion) VALUES (%s, %s, %s, %s)"
            valores = (id_entrevistador, diagnostico, id_paciente, diagnostico_depresion,)
            cursor.execute(consulta, valores)
            self.conexion.commit()
        except Exception as e:
            print(e)
    
    def obtener_por_id_paciente(self, id_paciente):
        try:
            cursor = self.conexion.cursor()
            
            consulta = "SELECT * FROM ( SELECT *, ROW_NUMBER() OVER (ORDER BY fecha_entrevista DESC) AS row_num, CEIL(ROW_NUMBER() OVER (ORDER BY fecha_entrevista ASC) / 3.0) AS group_num FROM entrevista WHERE id_paciente = %s ) AS subquery WHERE group_num = ( SELECT MAX(group_num) FROM ( SELECT CEIL(ROW_NUMBER() OVER (ORDER BY fecha_entrevista DESC) / 3.0) AS group_num FROM entrevista WHERE id_paciente = %s ) AS inner_query ) ORDER BY fecha_entrevista DESC;"
            values = (id_paciente, id_paciente)
            cursor.execute(consulta, values)
            return cursor.fetchall()
        except Exception as e:
            print(e)
    
  