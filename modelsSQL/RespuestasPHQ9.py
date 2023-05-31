from modelsSQL.Database import conexion
import hashlib

class RespuestasPHQ9:
    def __init__(self):

        self.conexion = conexion

    def obtener_por_valor(self, valor):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT respuesta FROM respuestas_phq9 WHERE valor = %s"
            valor = (valor,)
            cursor.execute(consulta, valor)
            resultado = cursor.fetchone()
            return resultado[0]
        except Exception as e:
            print(e)
     

    def obtener_todos(self):
        cursor = self.conexion.cursor()
        try:
            consulta = "SELECT * FROM respuestas_phq9"
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
                print(e)
