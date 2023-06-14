"""webDepresion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from frontend import views
from frontend.views import TomaVideo 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('web/', include('web.urls')),
    path('video/', views.upload_video, name="index"),
    path('', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('registro/', views.registro, name="registro"),
    path('recuperar_clave/', views.recuperar_contrasena, name="recuperar"),
    path('perfil/', views.perfil, name="perfil"),
    path('perfil_doctor/', views.perfil_doctor, name="perfil_doctor"),
    path('entrevista/', views.entrevista, name="entrevista"),
    path('gestion_pacientes/', views.pacientes, name="pacientes"),
    path('gestion_doctores/', views.doctores, name="doctores"),
    path('habilitar-deshabilitar-doctor/', views.hab_doctor, name="hab_doctor"),
    path('habilitar-deshabilitar-paciente/', views.hab_paciente, name="hab_paciente"),
    path('editar_perfil/', views.editar_perfil, name="editar_perfil"),
    path('diagnostico_paciente/', views.diagnostico, name="diagnostico"),
    path('videos_paciente/', views.videos_paciente, name="videos_paciente"),
    path('video_paciente/', views.video_paciente, name="video_paciente"),


]
