from django import forms
from .models import Notificacion

# class NotificacionForm(forms.Form):
class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = ['title', 'description']

    title = forms.CharField(
        label='titulo',
        max_length=60,
        min_length=3,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-1'})
    )
    description = forms.CharField(
        label='descripcion',
        max_length=600,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control mb-1'})
    )