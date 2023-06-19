from modelsSQL.Database import conexion

class PreguntasAsociadas:
    def __init__(self):
        self.conexion = conexion

    
    def obtener_9_aleatoriamente(self):
        try:
            cursor = self.conexion.cursor()
            preguntas = []
            for i in range(1, 10):
                consulta = '''
                    SELECT pregunta
                    FROM preguntas_asociadas_phq9 WHERE id_pregunta_asociada = %s
                    ORDER BY RAND()
                    LIMIT 1;
                '''
                valor = str(i)
                valores = (valor,)
                cursor.execute(consulta, valores)
                resultado = cursor.fetchall()
                preguntas.append({ 'id': valor,'pregunta': resultado[0][0]})

            return preguntas
        except Exception as e:
            print(e)
