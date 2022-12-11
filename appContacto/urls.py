from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.contact, name='contact'),
    path('enviar_correo/', views.send_mail, name='send_mail'),
]
