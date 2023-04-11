from django.shortcuts import render
from django.views.generic import TemplateView
import hashlib
import os
from audio import *
from video.video import Video
import ffmpeg
# Create your views here.

class TomaVideo(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super(TomaVideo, self).get_context_data()
        return context

    def get(self, request):
        return render(request, self.template_name) 

def upload_video(request):
    if request.method == 'POST' and request.FILES['video']:
        video = request.FILES['video']
        sha1_hash = hashlib.sha1()


        with open('videos/video.webm', 'wb+') as destination:
            for chunk in video.chunks():
                sha1_hash.update(chunk)
                destination.write(chunk)
        hash_str = sha1_hash.hexdigest()
        filename = f"videos\{hash_str}"
        # Carga el archivo de entrada
       
        with open(filename+".webm", 'wb+') as destination:
                for chunk in video.chunks():
                    sha1_hash.update(chunk)
                    destination.write(chunk)
        
        input_path = filename + ".webm"
        output_path = filename + ".mp4"

        input_stream = ffmpeg.input(input_path)

        # Crea el stream de salida y define los codecs
        output_stream = ffmpeg.output(
            input_stream, 
            output_path, 
            codec='libx264', 
            preset='medium', 
            movflags='faststart', 
            pix_fmt='yuv420p', 
            crf=23
        )

        # Ejecuta la conversión
        ffmpeg.run(output_stream)

        os.remove('videos/video.webm')
        os.remove(f'videos/{filename}.webm')

        preprocesar(filename)
        return render(request, 'index.html')
    return render(request, 'index.html')


def preprocesar(video):
    v = Video()

    # Se divide el video en pequeños clips de 180 s (3 min)
    v.dividir_video_clips(video, 5)

    '''
    .
    .
    .
    Realizar todo el proceso
    '''

    #Encriptar el video
    v.encriptar_video(video)

