from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class autores(models.Model):
    nombre = models.CharField(max_length=75)
    
    def __unicode__(self):
    	return self.nombre

class lectores(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    
    def __unicode__(self):
    	return self.nombre    	

class titulos(models.Model):
    titulo = models.CharField(max_length=90)
    autor = models.ForeignKey(autores, default=None, null=True, blank=True)
    lector = models.ForeignKey(lectores, default=None, null=True, blank=True)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    puntuacion =  models.PositiveIntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=75)
    portada = models.ImageField(upload_to='imagenes', blank=True)
    
    def __unicode__(self):
    	return self.titulo


