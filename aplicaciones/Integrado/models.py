from django.db import models

# Create your models here.
class Ubigeo(models.Model):
    calle=models.CharField(max_length=50)
    numero=models.SmallIntegerField()
    distrito=models.CharField(max_length=50)

class Colegio(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    ##ubigeo=models.OneToOneField(Ubigeo, on_delete=models.CASCADE)
    
