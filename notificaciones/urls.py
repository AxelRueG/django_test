from django.urls import path

from . import views

app_name = 'notificacion'

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:notificacion_id>/", views.show, name='show'),
]