import json
import API.video_detection as video_detection

class Video():

    def __init__(self):
        pass

    def obtener_respuesta_videos(self, ruta_video):
        # Envia la carpetas de los videos al modulo de detección
        respuesta = video_detection.get_video_data(ruta_video)
        
        # Analiza la respuesta en formato JSON
        respuesta_json = json.loads(respuesta)
        
        # Obtener los valores de respuesta e id_video
        respuesta = respuesta_json['respuesta']
        id_carpeta = respuesta_json['id_carpeta']
        
        resultado = {'respuesta': respuesta, 'id_video': id_carpeta}
        
        resultado = json.dumps(resultado)
        # Devolver el resultado como JSON
        return respuesta
    
    def obtener_datos_videos(self, ruta_video):
        respuesta_video = self.obtener_respuesta_videos(ruta_video)

        return respuesta_video
  


    
