import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "web_depresion"
            )
    print("Conexión exitosa!")
except Exception as e:
    print(e)




