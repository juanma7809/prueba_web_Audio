import json
import random

def get_audio_data(folder):
    num = random.randrange(0,2)
    respuesta = "Bajo nivel de depresión"
    if num == 1:
        respuesta = "Alto nivel de depresión"   
    data = {"id_carpeta": folder, "respuesta": respuesta}
    return json.dumps(data)