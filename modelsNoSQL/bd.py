from pymongo import MongoClient

# crear una conexión con la base de datos MongoDB
client = MongoClient('localhost', 27017)
db = client['mi_basededatos']

# crear una colección para cada objeto
videos = db['videos']
audios = db['audios']
video_respuestas = db['video_respuestas']

# crear un objeto de ejemplo y guardar en la colección correspondiente
video = {
    'id': 1,
    'contenido': b'mis bytes de video'
}
videos.insert_one(video)

audio = {
    'id': 2,
    'contenido': b'mis bytes de audio'
}
audios.insert_one(audio)

video_respuesta = {
    'id': 3,
    'contenido': b'mis bytes de respuesta de video'
}
video_respuestas.insert_one(video_respuesta)
