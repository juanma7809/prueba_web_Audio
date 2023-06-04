import json
import random

def get_video_data(ruta):
    num = random.randrange(0,2)
    respuesta = "Bajo nivel de depresión"
    if num == 1:
        respuesta = "Alto nivel de depresión"   
    data = {"id_carpeta": ruta, "respuesta": respuesta}
    return json.dumps(data)