from moviepy.editor import *
import json
import audio_detection


class Audio():

    def __init__(self):
        pass

    def extraer_audio_de_video(self, video_path, audio_path):
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)

    def obtener_respuesta_audios(self, carpeta_audios):
        # Envia la carpetas de los audios al modulo de detección
        respuesta = audio_detection.get_audio_data(carpeta_audios)
        
        # Analiza la respuesta en formato JSON
        respuesta_json = json.loads(respuesta)
        
        # Obtener los valores de respuesta e id_audio
        respuesta = respuesta_json['respuesta']
        id_carpeta = respuesta_json['id_carpeta']
        
        resultado = {'respuesta': respuesta, 'id_audio': id_carpeta}
        
        # Devolver el resultado como JSON
        return resultado
    
    def obtener_datos_audios(self, carpeta_audios, json_paciente):
        respuesta_audio = self.obtener_respuesta_audios(carpeta_audios)

        dic_paciente =  json.loads(json_paciente)
        dic_paciente.update(respuesta_audio)

        json_paciente = json.dumps(dic_paciente)

        with open(f'{dic_paciente["id"]}.json', 'w') as f:
            json.dump(json_paciente, f)



a = Audio()
dic_paciente = {
    "id": "1564sdfdf65666",
    "carpeta": "wavs-1564sdfdf65666",
    "Nombre": "Juan",
    "Apellidos": "Lopez",
    "Fecha entrevista": "11/02/2023",
    "diagnóstico del profesional": '''
    Lorem ipsum dolor sit amet consectetur 
    adipisicing elit. Possimus aperiam incidunt 
    sequi veritatis rerum nulla dolorum 
    deleniti neque odit mollitia.
    '''
}

a.obtener_datos_audios("wavs-1564sdfdf65666", json.dumps(dic_paciente))      


    
