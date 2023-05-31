from modelsSQL.Database import conexion
import hashlib

class TestPHQ9:
    def __init__(self):

        self.conexion = conexion

    def obtener_por_id(self, id_test):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT pregunta FROM test_phq9 WHERE id_test = %s"
            valores = (id_test,)
            cursor.execute(consulta, valores)
            resultado = cursor.fetchone()
            return resultado[0]
        except Exception as e:
            print(e)

    def obtener_todos(self):
        cursor = self.conexion.cursor()
        try:
            consulta = "SELECT * FROM test_phq9"
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
                print(e)

