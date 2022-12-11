from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('acercaDe/', views.acercaDe, name='acercaDe'),
    path('educación/<str:name_category>', views.education, name='education'),
    path('experiencias_laborales/<str:name_category>', views.experience, name='experience'),
    path('práctica_pre_profesional/<str:name_category>', views.pre_professional_practice, name='pre_professional_practice'),
    path('voluntariados/<str:name_category>', views.volunteering, name='volunteering'),
    path('habilidades_informáticas/<str:name_category>', views.computers_skill, name='computers_skill'),
    path('idiomas/<str:name_category>', views.language, name='language'),
    path('logros/<str:name_category>', views.achievement, name='achievement'),
    path('cursos/<str:name_category>', views.course, name='course'),
    path('congresos/<str:name_category>', views.congress, name='congress'),
    path('capacitaciones/<str:name_category>', views.training, name='training'),
    path('referencias/<str:name_category>', views.references, name='references'),
    path('otros_datos/<str:name_category>', views.other_data, name='other_data'),
]
