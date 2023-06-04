from io import BytesIO
from moviepy.video.io.VideoFileClip import VideoFileClip
from cryptography.fernet import Fernet
import os

class Video(object):

    def __init__(self):
        self.ruta = "C:/Users/home/Desktop/webDepresion/webDepresion/video/"
        self.key_file = 'key.key'

    def dividir_video_clips(self, folder, video, clip_duration, ext):
        # Cargar el archivo de video
        video_path = folder + video + ext
        video_clip = VideoFileClip(video_path)

        # Crear directorio para guardar los clips
        output_dir = "wavs-" + video 
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Generar lista de clips
        clips = []
        video_path = video + ext
        for i, start_time in enumerate(range(0, int(video_clip.duration), clip_duration)):
            end_time = min(start_time + clip_duration, video_clip.duration)
            clip = video_clip.subclip(start_time, end_time)
            clip_path = os.path.join(output_dir, video_path + f"CLIP{i+1}.mp4")
            clip.write_videofile(clip_path)
            clips.append(clip)

        # Liberar recursos
        video_clip.close()
        for clip in clips:
            clip.close()
        
    def generate_key(self):
        # Generar clave de cifrado
        key = Fernet.generate_key()

        # Guardar la clave en un archivo
        with open(self.key_file, 'wb') as f:
            f.write(key)

    def load_key(self):
        # Cargar la clave desde el archivo
        with open(self.key_file, 'rb') as f:
            key = f.read()
        return key

    def encriptar_video(self, video):
        # Generar clave de cifrado
        key = self.load_key()
        # Cargar archivo de video como bytes
        with open(video, 'rb') as f:
            video_bytes = f.read()

        # Cifrar los bytes del video
        cipher = Fernet(key)
        encrypted_video = cipher.encrypt(video_bytes)

        # Guardar el archivo cifrado
        with open(video + '_encrypted.mp4', 'wb') as f:
            f.write(encrypted_video)
    
    def desencriptar_video(self, video):
        # Generar clave de cifrado
        key = self.load_key()

        with open(video, 'rb') as f:
            encrypted_video = f.read()
        # Descifrar los bytes del video cifrado
        cipher = Fernet(key)
        decrypted_video = cipher.decrypt(encrypted_video)

        # Guardar el archivo descifrado
        with open('video_decrypted.mp4', 'wb') as f:
            f.write(decrypted_video)

   

