from moviepy.editor import *



class Audio():

    def __init__(self):
        pass

    def extraer_audio_de_video(self, video_path, audio_path):
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)

    
