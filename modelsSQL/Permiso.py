from Database import conexion

class Permiso:
    def __init__(self):
        self.conexion = conexion

    def crear(self, nombre):
        try:
            cursor = self.conexion.cursor()
            consulta = "INSERT INTO permiso (nombre) valoresUES (%s)"
            valores = (nombre,)
            cursor.execute(consulta, valores)
            self.mydb.commit()
            print(cursor.rowcount, "registro(s) insertado(s).")
        except Exception as e:
            print(e)
        
    def obtener_todos(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM permiso")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)
            
    def obtener_por_id(self, id_permiso):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM permiso WHERE id_permiso = %s"
            valores = (id_permiso,)
            cursor.execute(consulta, valores)
            row = cursor.fetchone()
            if row:
                print(row)
            else:
                print("Permiso no encontrado.")
        except Exception as e:
            print(e)
            
    def actualizar(self, atributo, nuevo_valor, id_permiso):
        try:
            cursor = self.conexion.cursor()
            consulta = f"UPDATE permisos SET {atributo} = '{nuevo_valor}' WHERE id_rol = {id_permiso}"
            cursor.execute(consulta)
            conexion.cnx.commit()
        except Exception as e:
            print(e)
        
    def borrar(self, id_permiso):
        try:
            cursor = self.conexion.cursor()
            consulta = "DELETE FROM permiso WHERE id_permiso = %s"
            valores = (id_permiso,)
            cursor.execute(consulta, valores)
            self.mydb.commit()
            print(cursor.rowcount, "registro(s) eliminado(s).")
        except Exception as e:
            print(e)
    
    def __del__(self):
        self.conexion.close()

