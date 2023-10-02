from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Notificacion
from .form import NotificacionForm

# Create your views here.


def index(request):

    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            notificacion = Notificacion()
            notificacion.title = form.cleaned_data['title']
            notificacion.description = form.cleaned_data['description']

            notificacion.save()

            return redirect(reverse('notificacion:index'))
    else:
        form = NotificacionForm()


    notificaciones = Notificacion.objects.all()

    return render(request, 'notificaciones/index.html', {
        'title': 'index page',
        'notificaciones': notificaciones,
        'form': form,
    })

def show(request, notificacion_id):
    notificacion = get_object_or_404(Notificacion, pk=id)
    return render(request, 'notificacion/show.html', {
        'title': 'notificacion: ' + notificacion.id,
        'notificacion': notificacion
    })
