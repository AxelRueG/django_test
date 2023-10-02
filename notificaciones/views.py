from django.http import HttpResponse
from django.shortcuts import render

from .models import Notificacion

# Create your views here.


def index(request):
    notificaciones = Notificacion.objects.all()

    return render(request, 'notificaciones/index.html', {
        'title': 'index page',
        'notificaciones': notificaciones,
    })

