from Database import conexion


class PreguntaFormulario:
    def __init__(self):
        self.conexion = conexion


    def crear(self, id_formulario, id_pregunta):
        try:
            consulta = "INSERT INTO preguntas_formulario (id_formualrio, id_pregunta) VALUES (%s, %s)"
            values = (id_formulario, id_pregunta)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.lastrowid
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_formulario_preguntas):
        try:
            consulta = "SELECT * FROM preguntas_formulario WHERE id_formulario_preguntas = %s"
            values = (id_formulario_preguntas,)
            self.conexion.cursor.execute(consulta, values)
            return self.conexion.cursor.fetchone()
        except Exception as e:
            print(e)
    
    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM preguntas formulario"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_formulario_preguntas):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE formulario_preguntas SET {atributo} = '{nuevo_valor}' WHERE id_formulario_preguntas = {id_formulario_preguntas}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)

    def borrar(self, id_formulario_preguntas):
        try:
            consulta = "DELETE FROM preguntas_formulario WHERE id_formulario_preguntas = %s"
            values = (id_formulario_preguntas,)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.rowcount
        except Exception as e:
            print(e)

    def __del__(self):
        self.conexion.close()

