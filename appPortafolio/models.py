from pyexpat import model
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import ImageField

# Create your models here.
class Briefcase(models.Model):
    name=models.CharField(max_length=100, verbose_name='Nombre')
    description=RichTextField(verbose_name='Descripción')
    repository_address= models.CharField(max_length=100, verbose_name='Dirección del repositorio')
    image=models.ImageField(default='null', verbose_name='Imagen', upload_to='photos_briefcase')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    class Meta:
        verbose_name='Portafolio'
        verbose_name_plural='Portafolios'
        db_table="briefcase"
    
    def __str__(self):
        return self.name