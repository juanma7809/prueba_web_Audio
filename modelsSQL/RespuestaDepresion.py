from Database import conexion


class Respuesta:
    def __init__(self):
        self.conexion = conexion


    def crear(self, id_paciente, id_video_respuesta, id_audio_respuesta, nivel_depresion, descripcion, fecha_diagnostico, id_entrevista):
        try:
            consulta = "INSERT INTO respuesta_depresion (id_paciente, id_video_respuesta, id_audio_respuesta, nivel_depresion, descripcion, fecha_diagnostico, id_entrevista) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (id_paciente, id_video_respuesta, id_audio_respuesta, nivel_depresion, descripcion, fecha_diagnostico, id_entrevista)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.lastrowid
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_respuesta):
        try:
            consulta = "SELECT * FROM respuesta_depresion WHERE id_respuesta = %s"
            values = (id_respuesta,)
            self.conexion.cursor.execute(consulta, values)
            return self.conexion.cursor.fetchone()
        except Exception as e:
            print(e)
    
    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM respuesta_depresion"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_respuesta):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE respuesta_depresion SET {atributo} = '{nuevo_valor}' WHERE id_respuesta = {id_respuesta}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)

    def borrar(self, id_respuesta):
        try:
            consulta = "DELETE FROM respuesta_depresion WHERE id_respuesta = %s"
            values = (id_respuesta,)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.rowcount
        except Exception as e:
            print(e)

    def __del__(self):
        self.conexion.close()

