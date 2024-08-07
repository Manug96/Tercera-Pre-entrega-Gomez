from django.db import models

# Create your models here.


class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()
    email = models.EmailField(null=True)

    def __str__(self):
        return f"Nombre del Producto: {self.nombre}- Numero de comision:  {self.comision}- Email de contacto:{self.email}"


class Historia(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=40, null=True)


class Redes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
