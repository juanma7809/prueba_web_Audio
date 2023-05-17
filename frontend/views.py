from frontend.prevideo import *
from django.views.generic import TemplateView
#from modelsSQL import Permiso, Rol, RolPermisos

class TomaVideo(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super(TomaVideo, self).get_context_data()
        return context

    def get(self, request):
        return render(request, self.template_name)
    
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