from Database import conexion

class PacienteVideo:
    def __init__(self):
        self.conexion = conexion

    def crear(self, id_paciente, id_video, id_entrevista):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO paciente_video (id_paciente, id_video, id_entrevista) VALUES (%s, %s, %s)"
            valores = (id_paciente, id_video, id_entrevista)
            cursor.execute(consulta, valores)
            self.conexion.commit()
            cursor.close()
        except Exception as e:
            print(e)

    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM paciente_video"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_paciente_video):
        try:
            cursor = self.conexion.cursor()
            consulta = f"SELECT * FROM paciente_video WHERE id_paciente_video = {id_paciente_video}"
            valores = (id_paciente_video,)
            cursor.execute(consulta, valores)
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_paciente_video):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE paciente_video SET {atributo} = '{nuevo_valor}' WHERE id_rol = {id_paciente_video}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)


    def borrar(self, id_paciente_video):
        consulta = f"DELETE FROM paciente_video WHERE id_paciente_video = {id_paciente_video}"
        self.conexion.execute_consulta(consulta)