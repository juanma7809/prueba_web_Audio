from modelsSQL.Database import conexion
import hashlib

class DiagnosticoPHQ9:
    def __init__(self):

        self.conexion = conexion

    def obtener_diagnostico(self, puntos):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT diagnostico FROM diagnostico_phq9 WHERE %s >= rango1 AND %s <= rango2"
            valores = (puntos, puntos)
            cursor.execute(consulta, valores)
            resultado = cursor.fetchone()
            return resultado[0]
        except Exception as e:
            print(e)
