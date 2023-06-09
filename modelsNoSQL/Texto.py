from pymongo import MongoClient
from gridfs import GridFS
import bson.binary

cliente = MongoClient('mongodb://localhost:27017')
class TextoNoSQL():

    def __init__(self,):
        self.database = cliente['web_depresion']

        # crear una colección para cada objeto
        self.coleccion = self.database['texto']

    def guardar_texto(self, ruta_texto, hash):
        # Tamaño del fragmento en bytes (1M)
        chunk_size = 1024 * 1024
        texto_data = b''  # Variable para almacenar los datos del texto

        
        with open(ruta_texto, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break  # Fin del archivo

                # Agregar el fragmento a la variable de datos del texto
                texto_data += chunk
                

    
        texto_doc = {
            'filename': ruta_texto,
            'data': texto_data, 
            'hash': hash
        }
        
        texto_id = self.coleccion.insert_one(texto_doc).inserted_id

            
        # Imprimir el ID asignado al texto guardado
        print("texto guardado con ID:", texto_id)
    
    def obtener_texto_por_hash(self, hash):
        # Consulta para obtener el documento
        document = self.coleccion.find_one({"hash": hash})

        # Verificación de existencia del documento
        if document:
            # Obtención del nombre del archivo
            filename = document.get("filename")

            # Obtención de los datos del archivo
            file_data = document.get("data")

            # Escritura de los datos en un archivo
            with open(filename, "wb") as file:
                file.write(file_data)
                print(f"Archivo guardado correctamente: {filename}")
        else:
            print("El documento no existe en la base de datos.")




    