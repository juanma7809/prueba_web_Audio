from modelsSQL.Database import conexion


class Formulario:
    def __init__(self):
        self.conexion = conexion


    def crear(self, nombre, id):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO formulario (nombre_formulario, id_paciente) VALUES (%s, %s)"
            values = (nombre, id)
            cursor.execute(consulta, values)
            self.conexion.commit()
            consulta =  "SELECT LAST_INSERT_ID()"
            cursor.execute(consulta)
            resultado = cursor.fetchone()
            return resultado[0]
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_formulario):
        try:
            consulta = "SELECT * FROM formulario WHERE id_formulario = %s"
            values = (id_formulario,)
            self.conexion.cursor.execute(consulta, values)
            return self.conexion.cursor.fetchone()
        except Exception as e:
            print(e)
    


    def actualizar_diagnostico(self, puntos, diagnostico, id_formulario):
        try:
            cursor = self.conexion.cursor()
            consulta = "UPDATE formulario SET puntos = %s, diagnostico = %s WHERE id_formulario = %s"
            valores = (puntos, diagnostico, id_formulario)
            cursor.execute(consulta, valores)
            conexion.commit()
        except Exception as e:
            print(e)



