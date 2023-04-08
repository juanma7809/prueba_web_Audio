from django.shortcuts import render
from django.views.generic import TemplateView
import hashlib
import os


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

        with open('video.mp4', 'wb+') as destination:
            for chunk in video.chunks():
                sha1_hash.update(chunk)
                destination.write(chunk)
        hash_str = sha1_hash.hexdigest()
        filename = f"videos/{hash_str}.mp4"
        os.remove('video.mp4')
        with open(filename, 'wb+') as destination:
            for chunk in video.chunks():
                sha1_hash.update(chunk)
                destination.write(chunk)
        return render(request, 'index.html')
    return render(request, 'index.html')

