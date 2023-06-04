import json
import API.audio_detection as audio_detection

class Audio():

    def __init__(self):
        pass

    def obtener_respuesta_audios(self, carpeta_audios):
        # Envia la carpetas de los audios al modulo de detección
        respuesta = audio_detection.get_audio_data(carpeta_audios)
        
        # Analiza la respuesta en formato JSON
        respuesta_json = json.loads(respuesta)
        
        # Obtener los valores de respuesta e id_audio
        respuesta = respuesta_json['respuesta']
        id_carpeta = respuesta_json['id_carpeta']
        
        resultado = {'respuesta': respuesta, 'id_audio': id_carpeta}

        resultado = json.dumps(resultado)
        
        # Devolver el resultado como JSON
        return respuesta
    
    def obtener_datos_audios(self, carpeta_audios):
        respuesta_audio = self.obtener_respuesta_audios(carpeta_audios)

        return respuesta_audio


    
