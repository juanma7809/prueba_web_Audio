from django.shortcuts import render
from django.views.generic import TemplateView
import hashlib
import os
from audio.conversor import Conversor
from video.video import Video
import ffmpeg
import subprocess
from audio.analizador import *
from modelsNoSQL.Video import VideoNoSQL

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
        filename = f"{hash_str}"
        # Carga el archivo de entrada
       
        with open("videos/"+filename+".webm", 'wb+') as destination:
                for chunk in video.chunks():
                    sha1_hash.update(chunk)
                    destination.write(chunk)
        
        input_path =  "videos/" + filename + ".webm"
        output_path = "videos/" + filename + ".mp4"

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
    vi = VideoNoSQL()
    vi.guardar_video_encriptado("videos/"+video+".mp4_encrypted.mp4", video)

# def verificar_permiso(rol_nombre, permiso_nombre):
#     try:
#         # Obtener el rol por su nombre
#         id_rol = Rol.objects.obtener_por_nombre(nombre=rol_nombre)[0]
        
#         # Obtener el permiso por su nombre
#         id_permiso = Permiso.objects.obtener_por_nombre(nombre=permiso_nombre)[0]
        
#         # Verificar si el rol tiene asignado el permiso
#         if RolPermisos.objects.validar_permiso(rol=id_rol, permiso=id_permiso):
#             return True
#         else:
#             return False
        
#     except (Rol.DoesNotExist, Permiso.DoesNotExist, RolPermisos.DoesNotExist):
#         return False