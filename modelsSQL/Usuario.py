from modelsSQL.Database import conexion
import hashlib

class Usuario:
    def __init__(self):

        self.conexion = conexion

    def crear(self, id_rol, nombres, apellidos, correo, contrasena, cedula, fecha_nacimiento):
        try:
            cursor = self.conexion.cursor()
            readable_hash = hashlib.sha256(contrasena.encode()).hexdigest()
            consulta = "INSERT INTO usuario (id_rol, nombres, apellidos, correo, contrasena, cedula, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (id_rol, nombres, apellidos, correo, readable_hash, cedula, fecha_nacimiento)
            cursor.execute(consulta, valores)
            self.conexion.commit()
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_usuario):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE usuario SET {atributo} = '{nuevo_valor}' WHERE id_usuario = {id_usuario}"
            cursor.execute(consulta)
            conexion.cnx.commit()
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
            consulta = "SELECT * FROM usuario WHERE id_usuario = %s"
            valor = (id_usuario,)
            self.conexion.cursor.execute(consulta, valor)
            resultado = self.conexion.cursor.fetchone()
            return resultado
        except Exception as e:
            print(e)

    def validar_usuario(self, correo, contrasena):
        try:
            cursor = self.conexion.cursor()
            contrasena = readable_hash = hashlib.sha256(contrasena.encode()).hexdigest()
            print(correo, contrasena)
            consulta = "SELECT * FROM usuario WHERE correo = %s and contrasena = %s"
            values = (correo, str(contrasena),)
            cursor.execute(consulta, values)
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False 
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
        try:
            consulta = "SELECT * FROM usuario"
            self.conexion.cursor.execute(consulta)
            resultados = self.conexion.cursor.fetchall()
            return resultados
        except Exception as e:
                print(e)