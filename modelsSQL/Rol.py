from Database import conexion


class Rol:
    def __init__(self):
        self.conexion = conexion


    def crear(self, id_rol, nombre_rol):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO rol (id_rol, nombre_rol) VALUES (%s, %s)"
            values = (id_rol, nombre_rol)
            cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.lastrowid
        except Exception as e:
            print(e)

    def obtener_por_id(self, id_rol):
        try:
            consulta = "SELECT * FROM rol WHERE id_rol = %s"
            values = (id_rol,)
            self.conexion.cursor.execute(consulta, values)
            return self.conexion.cursor.fetchone()
        except Exception as e:
            print(e)
    
    def obtener_por_nombre(self, nombre_rol):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM rol WHERE nombre_rol = %s"
            valores = (nombre_rol,)
            cursor.execute(consulta, valores)
            row = cursor.fetchone()
            if row:
                return row
            else:
                return "Permiso no encontrado."
        except Exception as e:
            print(e)
    
    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM rol"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(e)

    def actualizar(self, atributo, nuevo_valor, id_rol):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE rol SET {atributo} = '{nuevo_valor}' WHERE id_rol = {id_rol}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)

    def borrar(self, id_rol):
        try:
            consulta = "DELETE FROM rol WHERE id_rol = %s"
            values = (id_rol,)
            self.conexion.cursor.execute(consulta, values)
            self.conexion.commit()
            return self.conexion.cursor.rowcount
        except Exception as e:
            print(e)

    def __del__(self):
        self.conexion.close()


