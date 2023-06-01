from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import hashlib
import os
import json
from audio.conversor import Conversor
from video.video import Video
import ffmpeg
import subprocess
from audio.analizador import *
from modelsNoSQL.Video import VideoNoSQL
from modelsNoSQL.Audio import AudioNoSQL
from modelsNoSQL.Texto import TextoNoSQL
from modelsSQL.Usuario import Usuario
from modelsSQL.RolPermisos import RolPermisos
from modelsSQL.Permiso import Permiso
from modelsSQL.TestPHQ9 import TestPHQ9
from modelsSQL.RespuestasPHQ9 import RespuestasPHQ9
from modelsSQL.Formulario import Formulario
from modelsSQL.PreguntasFormulario import PreguntaFormulario
from modelsSQL.DiagnosticoPHQ9 import DiagnosticoPHQ9
from utilidades.Envio_correo import *

# Create your views here.

class TomaVideo(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super(TomaVideo, self).get_context_data()
        return context

    def get(self, request):
        return render(request, self.template_name) 


def login(request):
    if request.method == 'POST' and request.POST['user'] and request.POST['pass']:
        u = Usuario()
        valido, resultado = u.validar_usuario(request.POST['user'], request.POST['pass'])
        
        
        if valido:
            context = {
            'id_usuario': resultado[0],
            'id_rol': resultado[1],
            'nombre_completo': resultado[2] + resultado[3]
        }
            return redirect('/dashboard/?id={}&rol={}'.format(context['id_usuario'], context['id_rol']))
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def dashboard(request):
    id = request.GET.get('id')
    rol = request.GET.get('rol')
    rp = RolPermisos()
    tuplas = rp.obtener_permisos_rol(rol)

    lista_ids_permisos = [tupla[0] for tupla in tuplas]

    p = Permiso()
    permisos = [p.obtener_por_id(i) for i in lista_ids_permisos]

    lista_permisos = []

    for sublist in permisos:
        data_dict = {
            'id': sublist[0][0],
            'permiso': sublist[0][1],
            'titulo': sublist[0][2],
            'imagen': sublist[0][3],
            'enlace': sublist[0][4]
        }
        lista_permisos.append(data_dict)
    
    data = lista_permisos

    context = {
        'd': data
    }

    return render(request, 'dashboard.html', context)


def registro(request):
    if request.method == 'POST' and (request.POST['names'] and request.POST['lastnames'] and request.POST['borndate'] and request.POST['id'] and request.POST['mail'] and request.POST['pass']):
        if request.POST['pass'] == request.POST['pass2']:
            u = Usuario()
           
            u.crear(
                id_rol=3,
                nombres=request.POST['names'],
                apellidos=request.POST['lastnames'],
                correo=request.POST['mail'],
                contrasena=request.POST['pass'],
                cedula=request.POST['id'],
                fecha_nacimiento=request.POST['borndate'],
                genero=request.POST['genero']
            )
            return redirect('/')
        else: 
            return render(request, 'registro.html')
    else:
        return render(request, 'registro.html')

def recuperar_contrasena(request):
    if request.method == 'POST' and request.POST['user']:
        u = Usuario()
        nombre = u.obtener_nombre_usuario(request.POST['user'])   
        if nombre:
            
            nombre = nombre[0] + " " +  nombre[1]
            nueva = enviar_correo_recuperacion_contrasena(
            destino = 'juanjose.aroca@utp.edu.co',
            contrasena = '',
            correo = request.POST['user'],
            usuario = nombre)

            u.actualizar_contrasena(request.POST['user'], nueva)

            return redirect('/')
        else:
            return render(request, 'recuperar_con.html')    
    else:
        return render(request, 'recuperar_con.html')

def perfil(request):
    u = Usuario()
    id = request.GET.get('id')
    rol = request.GET.get('rol')
    if rol == "1":
        nombre_rol ="Admin"
    elif rol == "2":
        nombre_rol = "Doctor"
    elif rol == "3":
        nombre_rol = "Paciente"
    datos = u.obtener_por_id(id)
    data = {
        "nombres":  datos[2],
        "apellidos": datos[3],
        "correo": datos[4],
        "direccion": datos[5],
        "telefono": datos[6],
        "cedula": datos[8],
        "fecha_nacimiento": datos[9],
        "rol": nombre_rol

    }

    context = {
        "d": data
    }

    if request.method == 'POST':
        u.actualizar_perfil_usuario(
            nombres=request.POST['nombres'],
            apellidos=request.POST['apellidos'],
            correo=request.POST['correo'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            cedula=request.POST['cedula'],
            fecha_nacimiento=request.POST['fecha_nacimiento'],
            id_usuario=id
        )

        return redirect('/dashboard/?id={}&rol={}'.format(id, rol))

    return render(request, 'profile.html', context)

def perfil_doctor(request):
    return render(request, 'doctor_profile.html')

def entrevista(request):
    id = request.GET.get('id')
    rol = request.GET.get('rol')
    t = TestPHQ9()
    r = RespuestasPHQ9()
    preguntas = t.obtener_todos()
    lista_preguntas = []

    for tupla in preguntas:
        id_pregunta, pregunta = tupla
        diccionario = {"id": id_pregunta, "pregunta": pregunta}
        lista_preguntas.append(diccionario)
    
    respuestas = r.obtener_todos()
    lista_respuestas = []
    for tupla in respuestas:
        id_respuesta, respuesta, valor = tupla
        diccionario = {"id": id_respuesta, "respuesta": respuesta, "valor": valor}
        lista_respuestas.append(diccionario)
    
    context = {
        'p': lista_preguntas,
        'r': lista_respuestas
    }

    if request.method == 'POST':
        lista_valores = [request.POST[str(i)] for i in range(1,10) ]
        
        puntos = 0
        for i in lista_valores:
            puntos += int(i)
        
        u = Usuario()
        datos_usuario = u.obtener_por_id(id)
        nombre = datos_usuario[2] + " " + datos_usuario[3]
        form = Formulario()
        id_form = form.crear("Entrevista " + nombre, id)

        for i in range(len(lista_valores)):
            p = TestPHQ9()
            pregunta = p.obtener_por_id(str(i+1))
            r = RespuestasPHQ9()
            respuesta = r.obtener_por_valor(str(lista_valores[i]))
            pform = PreguntaFormulario()
            pform.crear(id_form, pregunta, respuesta)

        d = DiagnosticoPHQ9()

        diagnostico = d.obtener_diagnostico(str(puntos))

        form.actualizar_diagnostico(str(puntos), diagnostico, id_form)


        return redirect('/dashboard/?id={}&rol={}'.format(id, rol))
    return render(request, 'test.html', context)

def pacientes(request):
    u = Usuario()
    pacientes = u.obtener_pacientes()
    claves = ['id', 'nombre', 'apellido', 'cedula', 'correo', 'telefono']

    datos = [dict(zip(claves, row)) for row in pacientes]

    context =  {
        'd': datos
    }
    return render(request, 'crud_pacientes.html', context)

def doctores(request):
    u = Usuario()
    pacientes = u.obtener_doctores()
    claves = ['id', 'nombre', 'apellido', 'cedula', 'correo', 'telefono']

    datos = [dict(zip(claves, row)) for row in pacientes]

    context =  {
        'd': datos
    }
    return render(request, 'crud_doctores.html', context)

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


def preprocesar(hash):
    v = Video()

    # Se divide el video en pequeños clips de 180 s (3 min)
    v.dividir_video_clips("videos/", hash, 5, ".mp4")

    # Se convierten cada uno de esos videos en .wavs
    con = Conversor()

    # Retorna una lista con los audios
    audios = con.convert_all_mp4_to_wav("wavs-" + hash)

    print(audios)
    textos = process_audio_files(audios)



    #Encriptar el video
    v.encriptar_video("videos/"+hash+".mp4")

    #Guardar video en base de datos No SQL
    vi = VideoNoSQL()
    vi.guardar_video_encriptado("videos/"+hash+".mp4_encrypted.mp4", hash)

    #Guardar audios en base de datos No SQL
    audio_names = [(f, n) for n, f in enumerate(os.listdir(audios), start=1) if f.endswith('.wav')]

    a = AudioNoSQL()
    for audio in audio_names:
        a.guardar_audio(audios + "/" + audio[0], hash, audio[1])
    
    ti = TextoNoSQL()
    for t in textos:
        print(t)
        ti.guardar_texto(t, hash)
        #os.remove(t)


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