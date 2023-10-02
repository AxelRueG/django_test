from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.
class Notificacion(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=600)
    date_pub = models.DateField()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.date_pub = timezone.now()
        