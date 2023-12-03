import os
from django.http import HttpResponse

from .utils import main_func
from .models import String



def index(request, string):
    main_func(string)
    String.objects.create(title=string)
    file_path = 'C:/Dev/3_seconds_video/django_video/3_sec_video.mp4'
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="video/mp4")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
