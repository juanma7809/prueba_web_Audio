from django.shortcuts import render
import hashlib
import os
from audio.conversor import Conversor
from video.video import Video
import ffmpeg
import subprocess
from audio.analizador import *
from modelsNoSQL.Video import VideoNoSQL

# Create your views here.

 

def upload_video(request):
    if request.method == 'POST' and request.FILES['video']:
        video = request.FILES['video']
        sha1_hash = hashlib.sha1()


        with open('videos/video.webm', 'wb+') as destination:
            for chunk in video.chunks():
                sha1_hash.update(chunk)
                destination.write(chunk)
        hash_str = sha1_hash.hexdigest()
        filename = f"{hash_str}"
        # Carga el archivo de entrada
       
        with open("videos/"+filename+".webm", 'wb+') as destination:
                for chunk in video.chunks():
                    sha1_hash.update(chunk)
                    destination.write(chunk)
        
        input_path =  "videos/" + filename + ".webm"
        output_path = "videos/" + filename + ".mp4"

        print(filename)
        # Ejecuta el comando ffmpeg para la conversión
        subprocess.run(['ffmpeg', '-i', input_path, '-c:v', 'libx264', '-c:a', 'copy', output_path])


        # input_stream = ffmpeg.input(input_path)

        # # Crea el stream de salida y define los codecs
        # output_stream = ffmpeg.output(
        #     input_stream, 
        #     output_path, 
        #     codec='libx264', 
        #     preset='medium', 
        #     movflags='faststart', 
        #     pix_fmt='yuv420p', 
        #     crf=23
        # )

        # # Ejecuta la conversión
        # ffmpeg.run(output_stream)

        os.remove('videos/video.webm')
        os.remove(f'videos/{filename}.webm')

        preprocesar(filename)
        return render(request, 'index.html')
    return render(request, 'index.html')


def preprocesar(video):
    v = Video()

    # Se divide el video en pequeños clips de 180 s (3 min)
    v.dividir_video_clips("videos/", video, 5, ".mp4")

    # Se convierten cada uno de esos videos en .wavs
    con = Conversor()

    # Retorna una lista con los audios
    audios = con.convert_all_mp4_to_wav("wavs-" + video)

    print(audios)
    process_audio_files(audios)



    #Encriptar el video
    v.encriptar_video("videos/"+video+".mp4")
    vr = VideoNoSQL()
    vr.guardar_video_encriptado("videos/"+video+"_encrypted.mp4")

