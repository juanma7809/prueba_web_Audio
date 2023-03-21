from django.urls import path
from .views import PacienteView
urlpatterns = [
    path('paciente/', PacienteView.as_view(), name='pacientes_list')
]