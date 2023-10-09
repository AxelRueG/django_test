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

            return redirect('notificaciones:index')
    else:
        form = NotificacionForm()


    notificaciones = Notificacion.objects.all()

    return render(request, 'notificaciones/index.html', {
        'title': 'index page',
        'notificaciones': notificaciones,
        'form': form,
    })

def edit(request, id):
    notificacion = get_object_or_404(Notificacion, pk=id)

    if request.method == 'POST':
        form = NotificacionForm(request.POST, instance=notificacion)
        if form.is_valid():
            form.save()
            return redirect('notificaciones:index')
    else:
        form = NotificacionForm(instance= notificacion)

    return render(request, 'notificaciones/show.html', {
        'title': f'notificacion: {notificacion.id}',
        'form': form,
        'notificacion': notificacion,
    })

def delete(request, id):
    if request.method == 'POST':
        notificacion = get_object_or_404(Notificacion, pk=id)
        notificacion.delete()
        return redirect('notificaciones:index')
    else:
        return redirect('notificacion:index')