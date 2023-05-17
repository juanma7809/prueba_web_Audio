from pymongo import MongoClient
from gridfs import GridFS
import bson.binary

cliente = MongoClient('mongodb://localhost:27017')
class VideoNoSQL():

    def __init__(self,):
        self.database = cliente['web_depresion']

        # crear una colección para cada objeto
        self.coleccion = self.database['video']

    def guardar_video_encriptado(self, ruta_video):
        # Tamaño del fragmento en bytes (1M)
        chunk_size = 1024 * 1024
        video_data = b''  # Variable para almacenar los datos del video

        
        with open(ruta_video, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break  # Fin del archivo

                # Agregar el fragmento a la variable de datos del video
                video_data += chunk
                

    
        video_doc = {
            'filename': ruta_video,
            'data': video_data
        }
        
        video_id = self.coleccion.insert_one(video_doc).inserted_id

            
        # Imprimir el ID asignado al video guardado
        print("Video guardado con ID:", video_id)




    def __del__(self):
        cliente.close()


