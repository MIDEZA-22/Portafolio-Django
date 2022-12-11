from django.urls import path
from . import views

urlpatterns = [
    path('portafolio/', views.briefcase, name='briefcase'),
]
