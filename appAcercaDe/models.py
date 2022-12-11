from django.db import models
from ckeditor.fields import RichTextField
from django.forms import ImageField 

# Create your models here.
class Category_CV(models.Model):
    name=models.CharField(max_length=100, verbose_name='Nombre')
    order=models.IntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name='Categoría del CV'
        verbose_name_plural='Categorías del CV'
        db_table="category_CV"
    
    def __str__(self):
        return self.name

class Education(models.Model):
    name=models.CharField(max_length=200, verbose_name='Nombre')
    description=models.CharField(max_length=300, verbose_name='Descripción')
    level=models.CharField(max_length=100, blank=True, verbose_name='Nivel')
    note=models.CharField(max_length=20, blank=True, verbose_name='Nota')
    image=models.ImageField(default='null', verbose_name='Imagen', upload_to='photos_education')
    start_date=models.DateField(blank=False, null=False, verbose_name='Fecha de inicio') #az Un campo que no puede ser dejado en blanco ni tampoco puede recibir valores nulos
    finish_date=models.DateField(blank=False, null=False, verbose_name="Fecha de finalización") #az Un campo que no puede ser dejado en blanco ni tampoco puede recibir valores nulos
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Educación'
        verbose_name_plural='Educaciones'
        db_table="education"

    def __str__(self):
        return self.name

class Experience(models.Model):
    entity=models.CharField(max_length=200, verbose_name='Entidad')
    held_position=models.CharField(max_length=300, verbose_name='Cargo ocupado')
    functions=RichTextField(verbose_name='Funciones')
    start_date=models.DateField(blank=False, null=False, verbose_name='Fecha de inicio')
    finish_date=models.DateField(blank=False, null=False, verbose_name='Fecha de finalización')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Experiencia'
        verbose_name_plural='Experiencias'
        db_table="experience"

    def __str__(self):
        return self.entity

class Pre_Professional_Practice(models.Model):
    entity=models.CharField(max_length=200, verbose_name='Entidad')
    held_position=models.CharField(max_length=300, verbose_name='Cargo ocupado')
    functions=RichTextField(verbose_name='Funciones')
    start_date=models.DateField(blank=False, null=False, verbose_name='Fecha de inicio')
    finish_date=models.DateField(blank=False, null=False, verbose_name='Fecha de finalización')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Práctica Pre Profesional'
        verbose_name_plural='Prácticas Pre Profesionales'
        db_table="pre_professional_practice"

    def __str__(self):
        return self.entity

class Volunteering(models.Model):
    entity=models.CharField(max_length=200, verbose_name='Entidad')
    held_position=models.CharField(max_length=300, verbose_name='Cargo ocupado')
    functions=RichTextField(verbose_name='Funciones')
    start_date=models.DateField(blank=False, null=False, verbose_name='Fecha de inicio')
    finish_date=models.DateField(blank=False, null=False, verbose_name='Fecha de finalización')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Voluntariado'
        verbose_name_plural='Voluntariados'
        db_table="volunteering"

    def __str__(self):
        return self.entity

class Computers_Skill(models.Model):
    entity=models.CharField(max_length=200, blank=True, verbose_name='Entidad')
    name=models.CharField(max_length=300, verbose_name='Nombre')
    framework=models.CharField(max_length=400, blank=True, verbose_name='Entorno de trabajo')
    level=models.CharField(max_length=200, blank=True, verbose_name='Nivel')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Habilidad informática'
        verbose_name_plural='Habilidades informáticas'
        db_table="computers_skill"
    
    def __str__(self):
        return self.name

class Language(models.Model):
    entity=models.CharField(max_length=200, blank=True, verbose_name='Entidad')
    name=models.CharField(max_length=300, verbose_name='Nombre')
    level=models.CharField(max_length=200, blank=True, verbose_name='Nivel')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Idioma'
        verbose_name_plural='Idiomas'
        db_table="language"
    
    def __str__(self):
        return self.name

class Achievement(models.Model):
    name=models.CharField(max_length=300, verbose_name='Nombre')
    description=models.CharField(max_length=300, blank=True, verbose_name='Descripción')
    image=models.ImageField(default='null', verbose_name='Imagen', upload_to='photos_achievement')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Logro'
        verbose_name_plural='Logros'
        db_table="achievement"

    def __str__(self):
        return self.name

class Course(models.Model):
    entity=models.CharField(max_length=200, verbose_name='Entidad')
    name=models.CharField(max_length=300, verbose_name='Nombre')
    start_date=models.DateField(blank=False, null=False, verbose_name='Fecha de inicio')
    finish_date=models.DateField(blank=False, null=False, verbose_name='Fecha de finalización')
    duration=models.CharField(max_length=20, blank=True, verbose_name='Duración')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Curso'
        verbose_name_plural='Cursos'
        db_table="course"

    def __str__(self):
        return self.name

class Congress(models.Model):
    entity=models.CharField(max_length=200, verbose_name='Entidad')
    name=models.CharField(max_length=300, verbose_name='Nombre')
    start_date=models.DateField(blank=False, null=False, verbose_name='Fecha de inicio')
    finish_date=models.DateField(blank=False, null=False, verbose_name='Fecha de finalización')
    duration=models.CharField(max_length=20, blank=True, verbose_name='Duración')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Congreso'
        verbose_name_plural='Congresos'
        db_table="congress"

    def __str__(self):
        return self.name

class Training(models.Model):
    entity=models.CharField(max_length=200, verbose_name='Entidad')
    name=models.CharField(max_length=300, verbose_name='Nombre')
    start_date=models.DateField(blank=False, null=False, verbose_name='Fecha de inicio')
    finish_date=models.DateField(blank=False, null=False, verbose_name='Fecha de finalización')
    duration=models.CharField(max_length=20, blank=True, verbose_name='Duración')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Capacitación'
        verbose_name_plural='Capacitaciones'
        db_table="training"

    def __str__(self):
        return self.name

class References(models.Model):
    name=models.CharField(max_length=300, verbose_name='Apellidos y Nombres')
    held_position=models.CharField(max_length=300, verbose_name='Cargo ocupado')
    entity=models.CharField(max_length=200, verbose_name='Entidad')
    phone=models.CharField(max_length=13, verbose_name='Teléfono')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Referencia'
        verbose_name_plural='Referencias'
        db_table="references"

    def __str__(self):
        return self.name

class Other_Data(models.Model):
    name=models.CharField(max_length=300, verbose_name='Nombre')
    description=RichTextField(verbose_name='Descripción')
    image=models.ImageField(default='null', verbose_name='Imagen', upload_to='photos_other_data')
    public=models.BooleanField(verbose_name='¿Publicado?')
    order=models.IntegerField(default=0, verbose_name='Orden')
    category=models.ForeignKey(Category_CV, on_delete=models.CASCADE, verbose_name='Categoría del CV')

    class Meta:
        verbose_name='Otro Dato'
        verbose_name_plural='Otros Datos'
        db_table="other_data"

    def __str__(self):
        return self.name