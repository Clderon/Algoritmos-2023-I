# urls propios del app core 
from django.urls import path
# el punto representa la direccion actual de la app
from . import views

urlpatterns = [
    # path del core
    # se define rl utl y un nombre de views.home que renderiza un archivo.html
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("sample/", views.sample, name="sample"),
    path("visit/", views.visit, name="visit"),
]