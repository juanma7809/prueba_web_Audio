import json

def get_audio_data(folder):
    data = {"id_carpeta": folder, "respuesta": "Alto nivel de depresión"}
    return json.dumps(data)