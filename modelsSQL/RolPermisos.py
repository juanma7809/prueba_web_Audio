from Database import conexion


class RolPermisos:
    def __init__(self):
        
        self.conexion = conexion

    def crear(self, id_rol_permisos, id_rol, id_permiso):
        try:
            cursor = self.conexion.cursor
            consulta = "INSERT INTO rol_permisos (id_rol_permisos, id_rol, id_permiso) VALUES (%s, %s, %s)"
            valores = (id_rol_permisos, id_rol, id_permiso)
            cursor.execute(consulta, valores)
            self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_rol_permisos):
        try:
            cursor = self.conexion.cursor
            consulta = "SELECT * FROM rol_permisos WHERE id_rol_permisos = %s"
            valores = (id_rol_permisos,)
            cursor.execute(consulta, valores)
            return cursor.fetchone()
        except Exception as e:
            print(e)
    
    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM rol_permisos"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_rol_permisos):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE rol_permisos SET {atributo} = '{nuevo_valor}' WHERE id_rol_permisos = {id_rol_permisos}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)

    def borrar(self, id_rol_permisos):
        try:
            cursor = self.conexion.cursor
            consulta = "DELETE FROM rol_permisos WHERE id_rol_permisos = %s"
            valores = (id_rol_permisos,)
            cursor.execute(consulta, valores)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(e)

    def __del__(self):
        self.conexion.close()
