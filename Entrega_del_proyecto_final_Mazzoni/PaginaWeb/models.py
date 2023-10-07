from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nintendo(models.Model):
    Desarrolladora=models.CharField(max_length=60)
    Fecha_de_inauguración=models.DateField()
    Juego=models.CharField(max_length=50)
    Fecha_de_salida=models.DateField()

    def __str__(self):
        return f'{self.Desarrolladora} - {self.Juego} '
    
class Playstation(models.Model):
    Desarrolladora=models.CharField(max_length=60)
    Fecha_de_inauguración=models.DateField()
    Juego=models.CharField(max_length=50)
    Fecha_de_salida=models.DateField()

    def __str__(self):
        return f'{self.Desarrolladora} - {self.Juego}'

class Xbox(models.Model):
    Desarrolladora=models.CharField(max_length=60)
    Fecha_de_inauguración=models.DateField()
    Juego=models.CharField(max_length=50)
    Fecha_de_salida=models.DateField()

    def __str__(self):
        return f'{self.Desarrolladora} - {self.Juego}'
    
    #{self.Fecha_de_inauguracion} - {self.Fecha_de_salida}

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", blank=True, null=True)