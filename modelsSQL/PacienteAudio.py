from Database import conexion

class PacienteAudio:
    def __init__(self):
        self.conexion = conexion

    def crear(self, id_paciente, id_audio, id_entrevista):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO paciente_audio (id_paciente, id_audio, id_entrevista) VALUES (%s, %s, %s)"
            valores = (id_paciente, id_audio, id_entrevista)
            cursor.execute(consulta, valores)
            self.conexion.commit()
            cursor.close()
        except Exception as e:
            print(e)

    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM paciente_audio"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_paciente_audio):
        try:
            cursor = self.conexion.cursor()
            consulta = f"SELECT * FROM paciente_audio WHERE id_paciente_audio = {id_paciente_audio}"
            valores = (id_paciente_audio,)
            cursor.execute(consulta, valores)
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_paciente_audio):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE paciente_audio SET {atributo} = '{nuevo_valor}' WHERE id_paciente_audio = {id_paciente_audio}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)


    def borrar(self, id_paciente_audio):
        try:
            consulta = f"DELETE FROM paciente_audio WHERE id_paciente_audio = {id_paciente_audio}"
            values = (id_paciente_audio,)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.rowcount
        except Exception as e:
            print(e)