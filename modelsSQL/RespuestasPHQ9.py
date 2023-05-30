from modelsSQL.Database import conexion
import hashlib

class RespuestasPHQ9:
    def __init__(self):

        self.conexion = conexion

    

    def actualizar(self, atributo, nuevo_valor, id_usuario):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE usuario SET {atributo} = '{nuevo_valor}' WHERE id_usuario = {id_usuario}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)
    
    def actualizar_perfil_usuario(self, nombres, apellidos, correo, direccion, telefono, cedula, fecha_nacimiento, id_usuario):
        try:
            cursor = self.conexion.cursor()
    
            consulta = "UPDATE usuario SET nombres = %s, apellidos = %s, correo = %s, direccion = %s, telefono = %s, cedula = %s, fecha_nacimiento  = %s WHERE id_usuario = %s"
            valores = (nombres, apellidos, correo, direccion, telefono, cedula, fecha_nacimiento, id_usuario,)
            cursor.execute(consulta, valores)
            self.conexion.commit()
        except Exception as e:
            print(e)
    
    def actualizar_contrasena(self, correo, nueva_contrasena):
        try:
            cursor = self.conexion.cursor()
            nueva_contrasena = hashlib.sha256(nueva_contrasena.encode()).hexdigest()
            consulta = "UPDATE usuario SET contrasena = %s WHERE correo = %s"
            valores = (nueva_contrasena, correo,)
            cursor.execute(consulta, valores)
            self.conexion.commit()
        except Exception as e:
            print(e)

    def borrar(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "DELETE FROM usuario WHERE id_usuario = %s"
            valor = (self.id_usuario,)
            cursor.execute(consulta, valor)
            self.conexion.self.conexion.commit()
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_usuario):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM usuario WHERE id_usuario = %s"
            valor = (id_usuario,)
            cursor.execute(consulta, valor)
            resultado = cursor.fetchone()
            return resultado
        except Exception as e:
            print(e)

    def validar_usuario(self, correo, contrasena):
        try:
            cursor = self.conexion.cursor()
            contrasena = readable_hash = hashlib.sha256(contrasena.encode()).hexdigest()
            consulta = "SELECT * FROM usuario WHERE correo = %s and contrasena = %s"
            values = (correo, str(contrasena),)
            cursor.execute(consulta, values)
            result = cursor.fetchone()
            if result:
                return True, result
            else:
                return False, None 
        except Exception as e:
            print(e)

    def obtener_nombre_usuario(self, correo):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT nombres, apellidos FROM usuario WHERE correo = %s"
            values = (correo,)
            cursor.execute(consulta, values)
            result = cursor.fetchone()
            return result
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