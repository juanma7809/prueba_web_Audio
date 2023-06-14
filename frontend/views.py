from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import hashlib
import os
import base64
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
from modelsSQL.Entrevista import Entrevista
from modelsSQL.PacienteAudio import PacienteAudio
from modelsSQL.PacienteVideo import PacienteVideo
from utilidades.Envio_correo import *
from API.Audio import Audio as APIAudio
from API.Video import Video as APIVideo

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
    if request.method == 'POST' and (request.POST['names'] and request.POST['lastnames'] and request.POST['borndate'] and request.POST['id'] and request.POST['mail'] and request.POST['pass'], request.POST['rol']):
        if request.POST['pass'] == request.POST['pass2']:
            u = Usuario()
            if request.POST['rol'] == '3': 
                activo = '1' 
            else: 
                activo = '0'
            u.crear(
                id_rol=request.POST['rol'],
                nombres=request.POST['names'],
                apellidos=request.POST['lastnames'],
                correo=request.POST['mail'],
                contrasena=request.POST['pass'],
                cedula=request.POST['id'],
                fecha_nacimiento=request.POST['borndate'],
                genero=request.POST['genero'],
                activo=activo
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
            origen = 'juanjose.aroca@utp.edu.co',
            contrasena = '12mfy45-',
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
    rol = request.GET.get('rol')
    u = Usuario()
    pacientes = u.obtener_pacientes()
    claves = ['id', 'nombre', 'apellido', 'cedula', 'correo', 'telefono', 'activo']

    datos = [dict(zip(claves, row)) for row in pacientes]

    context =  {
        'd': datos,
        'r': {'rol': rol}
    }
    return render(request, 'crud_pacientes.html', context)

def doctores(request):
    rol = request.GET.get('rol')
    u = Usuario()
    pacientes = u.obtener_doctores()
    claves = ['id', 'nombre', 'apellido', 'cedula', 'correo', 'telefono', 'activo']

    datos = [dict(zip(claves, row)) for row in pacientes]

    context =  {
        'd': datos,
        'r': {'rol': rol}
    }


    return render(request, 'crud_doctores.html', context)

def hab_doctor(request):
    id = request.GET.get('id')
    rol = request.GET.get('rol')
    id_usu = request.GET.get('id_usu')
    activo = request.GET.get('activo')

    if activo == '0':
        activo = '1'
    else:
        activo = '0'
    
    u = Usuario()
    u.hab_usuario(id_usu, activo)

    pacientes = u.obtener_doctores()
    claves = ['id', 'nombre', 'apellido', 'cedula', 'correo', 'telefono', 'activo']

    datos = [dict(zip(claves, row)) for row in pacientes]


    context =  {
        'd': datos,
        'r': {'rol': rol}
    }
    return render(request, 'crud_doctores.html', context)

def hab_paciente(request):
    id = request.GET.get('id')
    rol = request.GET.get('rol')
    id_usu = request.GET.get('id_usu')
    activo = request.GET.get('activo')

    if activo == '0':
        activo = '1'
    else:
        activo = '0'
    
    u = Usuario()
    u.hab_usuario(id_usu, activo)

    pacientes = u.obtener_pacientes()
    claves = ['id', 'nombre', 'apellido', 'cedula', 'correo', 'telefono', 'activo']

    datos = [dict(zip(claves, row)) for row in pacientes]

    context =  {
        'd': datos,
        'r': {'rol': rol}
    }
    return render(request, 'crud_pacientes.html', context)

def editar_perfil(request):
    u = Usuario()
    id = request.GET.get('id')
    rol = request.GET.get('rol')
    id_usu = request.GET.get('id_usu')
    
    
    datos = u.obtener_por_id(id_usu)
    if datos[1] == 1:
        nombre_rol ="Admin"
    elif datos[1] == 2:
        nombre_rol = "Doctor"
    elif datos[1] == 3:
        nombre_rol = "Paciente"
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
            id_usuario=id_usu
        )


        return redirect('/dashboard/?id={}&rol={}'.format(id, rol))

    return render(request, 'editar_perfil.html', context)

def diagnostico(request):
    u = Usuario()
    id = request.GET.get('id')
    rol = request.GET.get('rol')
    id_usu = request.GET.get('id_usu')
    e = Entrevista()
    pa = PacienteAudio()
    pv = PacienteVideo()
    
    
    datos = u.obtener_por_id(id_usu)
    if datos[1] == 1:
        nombre_rol ="Admin"
    elif datos[1] == 2:
        nombre_rol = "Doctor"
    elif datos[1] == 3:
        nombre_rol = "Paciente"
    
    f = Formulario()
    forms = f.obtener_por_id_paciente(id_usu)

    info_forms = ""

    if len(forms) > 0:
        for f in forms:
            info = f[1] + "\n"
            info += "Fecha de realización: " + str(f[5]) + "\n"
            info += "Diagnostico: " + f[4] + "\n"
            info += "Puntos: " + str(f[3]) + "\n"
            info += "----------------------------" + "\n"

            info_forms += info
    
    entrevistas = e.obtener_por_id_paciente(id_usu)
    info_en = ""

    if len(entrevistas) > 0:
        for e in entrevistas:
            info = "Entrevista presencial de " + datos[2] + " " + datos[3] + "\n"
            datos_entrevistador = u.obtener_por_id(e[1])
            info += "Realizada por el profesional: " + datos_entrevistador[2] + " " +  datos_entrevistador[3] + "\n"
            info += "Fecha de realización: " + str(e[2]) + "\n"
            info += "Diagnostico: " + e[3] + "\n"
            info += "----------------------------" + "\n"

            info_en += info

    

    info_modulo = ""
    respuestas_audios = pa.obtener_por_id_paciente(id_usu)
    print(respuestas_audios)
    if respuestas_audios:
        for e in respuestas_audios:
            info = "Detección por medio de audio \n" 
            info += "Entrevista por video de " + datos[2] + " " + datos[3] + "\n"
            info += "Fecha de realización: " +  str(e[3]) + "\n"
            info += "Diagnóstico: " + e[4] + "\n"
            info += "----------------------------" + "\n"
            info_modulo += info
    
    respuestas_videos = pv.obtener_por_id_paciente(id_usu)
    if respuestas_videos:
        for e in respuestas_videos:
            info = "Detección por medio de video \n" 
            info += "Entrevista por video de " + datos[2] + " " + datos[3] + "\n"
            info += "Fecha de realización: " +  str(e[4]) + "\n"
            info += "Diagnóstico: " + e[5] + "\n"
            info += "----------------------------" + "\n"
            info_modulo += info
    

    data = {
        "nombres":  datos[2],
        "apellidos": datos[3],
        "correo": datos[4],
        "direccion": datos[5],
        "telefono": datos[6],
        "cedula": datos[8],
        "fecha_nacimiento": datos[9],
        "genero": datos[10],
        "rol": nombre_rol,
        "info_forms": info_forms,
        "info_entrevistas": info_en,
        "info_modulo": info_modulo

    }


    context = {
        "d": data
    }

    if request.method == 'POST' and request.POST['diagnostico']:
        e = Entrevista()
        u = Usuario()
        e.crear(
            id_entrevistador=id,
            diagnostico=request.POST['diagnostico'],
            id_paciente=id_usu
        )
        
        datos = u.obtener_por_id(id_usu)
        if datos[1] == 1:
            nombre_rol ="Admin"
        elif datos[1] == 2:
            nombre_rol = "Doctor"
        elif datos[1] == 3:
            nombre_rol = "Paciente"
        
        f = Formulario()
        forms = f.obtener_por_id_paciente(id_usu)

        info_forms = ""

        if len(forms) > 0:
            for f in forms:
                info = f[1] + "\n"
                info += "Fecha de realización: " + str(f[5]) + "\n"
                info += "Diagnostico: " + f[4] + "\n"
                info += "Puntos: " + str(f[3]) + "\n"
                info += "----------------------------" + "\n"

                info_forms += info

        entrevistas = e.obtener_por_id_paciente(id_usu)
        info_en = ""

        if len(entrevistas) > 0:
            for e in entrevistas:
                info = "Entrevista presencial de " + datos[2] + " " + datos[3] + "\n"
                datos_entrevistador = u.obtener_por_id(e[1])
                info += "Realizada por el profesional: " + datos_entrevistador[2] + " " + datos_entrevistador[3] + "\n"
                info += "Fecha de realización: " + str(e[2]) + "\n"
                info += "Diagnostico: " + e[3] + "\n"
                info += "----------------------------" + "\n"

                info_en += info


        data = {
            "nombres":  datos[2],
            "apellidos": datos[3],
            "correo": datos[4],
            "direccion": datos[5],
            "telefono": datos[6],
            "cedula": datos[8],
            "fecha_nacimiento": datos[9],
            "genero": datos[10],
            "rol": nombre_rol,
            "info_forms": info_forms,
            "info_entrevistas": info_en,
            "info_modulo": info_modulo

        }

        context = {
            "d": data
        }


        return render(request, 'diagnostico.html', context)



    
    return render(request, 'diagnostico.html', context)


def videos_paciente(request):
    id = request.GET.get('id')
    rol = request.GET.get('rol')
    id_usu = request.GET.get('id_usu')

    u = Usuario()
    pv = PacienteVideo()
    datos = u.obtener_por_id(id_usu)
    videos = pv.obtener_por_id_paciente(id_usu)


    data = {
            "nombres":  datos[2],
            "apellidos": datos[3],
            "correo": datos[4],
            "direccion": datos[5],
            "telefono": datos[6],
            "cedula": datos[8],
            "fecha_nacimiento": datos[9],
            "genero": datos[10]
        }
    lista_videos = []
    for video in videos:
        doctor = u.obtener_por_id(video[2])
        doctor = doctor[2] + ' ' + doctor[3]

        fecha = str(video[4])

        dic = {
            "doctor": doctor,
            "fecha": fecha,
            "video": video[3] + '.mp4'
        }
        lista_videos.append(dic)


    context = {
        'd': data,
        'v': lista_videos
    }
    return render(request, 'videos_container.html', context) 

def video_paciente(request):
    id_video = request.GET.get('id_video')

    url = "videos/" + id_video
    
    if os.path.exists(url):
        # Leer los bytes del video
        with open(url, 'rb') as file:
            video_bytes = file.read()
        
        # Convertir los bytes a una cadena en base64
        video_base64 = base64.b64encode(video_bytes).decode('utf-8')
        
        # Pasar la cadena en base64 al contexto
        context = {'video_bytes': video_base64}

        return render(request, 'video_paciente.html', context)


    
def upload_video(request):
    id = request.GET.get('id')
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

        preprocesar(filename, id)
        return render(request, 'index.html')
    return render(request, 'index.html')


def preprocesar(hash, id):
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
        os.remove(t)
    

    #Vinculación con los modulos de preprocesamiento de video
    api_audio = APIAudio()
    respuesta_audio = api_audio.obtener_datos_audios(audios)
    pa = PacienteAudio()
    pa.crear(id, hash, respuesta_audio)
    api_video = APIVideo()
    respuesta_video = api_video.obtener_datos_videos("videos/"+hash+".mp4")
    pv = PacienteVideo()
    pv.crear(id, hash, respuesta_video)
    



