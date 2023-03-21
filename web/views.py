from django.views import View
from .models import Paciente 
from django.http import JsonResponse

class PacienteView(View):

    def get(self, request):
        pacientes = list(Paciente.objects.values())
        if len(pacientes) > 0:
            datos = {'message': 'Success', 'pacientes': pacientes}
        else:
            datos = {'message': 'Pacientes not found'}
        return JsonResponse(datos)    
    
    def post(self, request):
        pass

    def put(self, request):
        pass

    def  delete(self, request):
        pass