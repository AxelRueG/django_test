from django import forms

class NotificacionForm(forms.Form):
    title = forms.CharField(label='titulo', max_length=60, min_length=3, required=True)
    description = forms.CharField(label='descripcion', max_length=600, required=False)