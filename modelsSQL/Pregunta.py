from Database import conexion


class Pregunta:
    def __init__(self):
        self.conexion = conexion


    def crear(self, pregunta):
        try:
            consulta = "INSERT INTO pregunta (pregunta) VALUES (%s)"
            values = (pregunta)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.lastrowid
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_pregunta):
        try:
            consulta = "SELECT * FROM pregunta WHERE id_pregunta = %s"
            values = (id_pregunta,)
            self.conexion.cursor.execute(consulta, values)
            return self.conexion.cursor.fetchone()
        except Exception as e:
            print(e)
    
    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM pregunta"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_pregunta):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE pregunta SET {atributo} = '{nuevo_valor}' WHERE id_pregunta = {id_pregunta}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)

    def borrar(self, id_pregunta):
        try:
            consulta = "DELETE FROM pregunta WHERE id_pregunta = %s"
            values = (id_pregunta,)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.rowcount
        except Exception as e:
            print(e)

    def __del__(self):
        self.conexion.close()

