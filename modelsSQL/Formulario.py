from Database import conexion


class Formulario:
    def __init__(self):
        self.conexion = conexion


    def crear(self, formualrio):
        try:
            consulta = "INSERT INTO formualrio (formualrio) VALUES (%s)"
            values = (formualrio)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.lastrowid
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
    
    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM formulario"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_formulario):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE pregunta SET {atributo} = '{nuevo_valor}' WHERE id_formulario = {id_formulario}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)

    def borrar(self, id_formulario):
        try:
            consulta = "DELETE FROM formulario WHERE id_formulario = %s"
            values = (id_formulario,)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.rowcount
        except Exception as e:
            print(e)

    def __del__(self):
        self.conexion.close()

