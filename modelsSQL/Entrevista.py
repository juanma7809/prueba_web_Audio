from Database import conexion

class Formulario:
    def __init__(self):
        self.conexion = conexion
    
    def crear(self, nombre_formulario):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO formulario(nombre_formulario) VALUES (%s)"
            valores = (nombre_formulario,)
            cursor.execute(consulta, valores)
            self.conexion.commit()
            cursor.close()
            print("Formulario creado exitosamente!")
        except Exception as e:
            print(e)
    
    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM formulario"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)
    
    def obtener_por_id(self, id_formulario):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM formulario WHERE id_formulario = %s"
            valores = (id_formulario,)
            cursor.execute(consulta, valores)
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except Exception as e:
            print(e)
    
    def actualizar(self, atributo, nuevo_valor, id_entrevista):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE entrevista SET {atributo} = '{nuevo_valor}' WHERE id_entrevista = {id_entrevista}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)
    
    def borrar(self, id_formulario):
        try:
            cursor = self.conexion.conexion.cursor()
            consulta = "DELETE FROM formulario WHERE id_formulario = %s"
            valores = (id_formulario,)
            cursor.execute(consulta, valores)
            self.conexion.conexion.commit()
            cursor.close()
            print("Formulario eliminado exitosamente!")
        except Exception as e:
            print(e)
    
    def __del__(self):
        self.conexion.close()