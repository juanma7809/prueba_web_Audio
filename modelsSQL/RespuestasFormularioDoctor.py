from modelsSQL.Database import conexion


class RespuestasFormularioDoctor:
    def __init__(self):
        self.conexion = conexion


    def crear(self, id_paciente, id_formulario_doctor, pregunta, respuesta):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO respuestas_formulario_doctor (id_paciente, id_formulario_doctor, pregunta, respuesta) VALUES (%s, %s, %s, %s)"
            values = (id_paciente, id_formulario_doctor, pregunta, respuesta,)
            cursor.execute(consulta, values)
            self.conexion.commit()
        except Exception as e:
            print(e)



    def obtener_por_id_formulario(self, id_formulario_doctor):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM respuestas_formulario_doctor WHERE id_formulario_doctor = %s"
            values = (id_formulario_doctor,)
            cursor.execute(consulta, values)
            return cursor.fetchall()
        except Exception as e:
            print(e)
    



