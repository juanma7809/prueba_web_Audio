from pymongo import MongoClient
from gridfs import GridFS
import bson.binary

cliente = MongoClient('mongodb://localhost:27017')
class AudioNoSQL():

    def __init__(self,):
        self.database = cliente['web_depresion']

        # crear una colección para cada objeto
        self.coleccion = self.database['audio']

    def guardar_audio(self, ruta_audio):
        # Tamaño del fragmento en bytes (1M)
        chunk_size = 1024 * 1024
        audio_data = b''  # Variable para almacenar los datos del audio

        
        with open(ruta_audio, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break  # Fin del archivo

                # Agregar el fragmento a la variable de datos del audio
                audio_data += chunk
                

    
        audio_doc = {
            'filename': ruta_audio,
            'data': audio_data
        }
        
        audio_id = self.coleccion.insert_one(audio_doc).inserted_id

            
        # Imprimir el ID asignado al audio guardado
        print("audio guardado con ID:", audio_id)




    def __del__(self):
        cliente.close()

a = AudioNoSQL()
a.guardar_audio("p/p.wav")
