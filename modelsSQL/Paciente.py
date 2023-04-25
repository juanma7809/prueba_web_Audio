from Database import conexion

class Paciente:
    def __init__(self):

        self.conexion = conexion

    def crear(self, id_rol, nombres, apellidos, correo, contrasena, cedula, fecha_nacimiento):
        try:
            consulta = "INSERT INTO paciente (id_rol, nombres, apellidos, correo, contrasena, cedula, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (id_rol, nombres, apellidos, correo, contrasena, cedula, fecha_nacimiento)
            self.conexion.cursor.execute(consulta, valores)
            self.conexion.self.conexion.commit()
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_paciente):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE paciente SET {atributo} = '{nuevo_valor}' WHERE id_paciente = {id_paciente}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)

    def borrar(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "DELETE FROM paciente WHERE id_paciente = %s"
            valor = (self.id_paciente,)
            cursor.execute(consulta, valor)
            self.conexion.self.conexion.commit()
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_paciente):
        try:
            consulta = "SELECT * FROM paciente WHERE id_paciente = %s"
            valor = (id_paciente,)
            self.conexion.cursor.execute(consulta, valor)
            resultado = self.conexion.cursor.fetchone()
            return resultado
        except Exception as e:
            print(e)

    def obtener_todos(self):
        try:
            consulta = "SELECT * FROM paciente"
            self.conexion.cursor.execute(consulta)
            resultados = self.conexion.cursor.fetchall()
            return resultados
        except Exception as e:
                print(e)
    
    def __del__(self):
        self.conexion.close()