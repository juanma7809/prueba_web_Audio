from Database import conexion

class PacienteFormulario:
    def __init__(self):
        self.conexion = conexion

    def crear(self, id_paciente, id_formulario, id_entrevista):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO paciente_formulario (id_paciente, id_formulario, id_entrevista) VALUES (%s, %s, %s)"
            valores = (id_paciente, id_formulario, id_entrevista)
            cursor.execute(consulta, valores)
            self.conexion.commit()
            cursor.close()
        except Exception as e:
            print(e)

    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM paciente_formulario"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_paciente_formulario):
        try:
            cursor = self.conexion.cursor()
            consulta = f"SELECT * FROM paciente_formulario WHERE id_paciente_formulario = {id_paciente_formulario}"
            valores = (id_paciente_formulario,)
            cursor.execute(consulta, valores)
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_paciente_formulario):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE paciente_formulario SET {atributo} = '{nuevo_valor}' WHERE id_paciente_formulario = {id_paciente_formulario}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)


    def borrar(self, id_paciente_formulario):
        try:
            consulta = f"DELETE FROM paciente_formulario WHERE id_paciente_formulario = {id_paciente_formulario}"
            values = (id_paciente_formulario,)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.rowcount
        except Exception as e:
            print(e)