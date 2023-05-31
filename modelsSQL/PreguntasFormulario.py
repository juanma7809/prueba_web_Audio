from modelsSQL.Database import conexion


class PreguntaFormulario:
    def __init__(self):
        self.conexion = conexion


    def crear(self, id_formulario, pregunta, respuesta):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO preguntas_formulario (id_formulario, pregunta, respuesta) VALUES (%s, %s, %s)"
            values = (id_formulario, pregunta, respuesta)
            cursor.execute(consulta, values)
            self.conexion.commit()
        except Exception as e:
            print(e)


