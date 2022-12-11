from django.urls import path
from . import views

urlpatterns = [
    path('',views.cover_page, name="login"),
    path('portada/', views.cover_page, name='cover_page'),

    path('login/', views.login_page, name="login"), 
    path('logout/', views.logout_user, name="logout"),
]
