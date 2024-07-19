from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo= models.CharField(primary_key=True, max_length=10)
    marca= models.CharField(max_length=20)
    nombre= models.CharField(max_length=300)
    precio= models.PositiveBigIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)


    