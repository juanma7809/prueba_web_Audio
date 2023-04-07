from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.

class TomaVideo(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super(TomaVideo, self).get_context_data()
        return context