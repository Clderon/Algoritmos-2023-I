"""
URL configuration for RescateAdopcion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# la funcion include nos permite agregar urlpatters de otras apps
from django.urls import path, include

# importando la configuracion creada en settings
from django.conf import settings

""" Incluyendo otra URLconf
    1. Importe la función include(): desde django.urls importe include, ruta
    2. Agregue una URL a urlpatterns: ruta('blog/', include('blog.urls'))
"""
urlpatterns = [
    # path del admin
    path("admin/", admin.site.urls),
    # path de services
    path("services/", include("services.urls")),
    # path de services
    path("blog/", include("blog.urls")),
    # path del core (no se pone '' para que carge en la raiz su urlpatterns)
    path("", include("core.urls")),
]

# configuracion para servir archivos estaticos en el directorio media

# Si tenemos el debug en marcha activamos la opcion de servir ficheros media en la url (MEDIA_URL = '/media/')
# y que iran a buscarlo al directorio (MEDIA_ROOT = os.path.join(BASE_DIR, 'media'))
if settings.DEBUG:
    # Cargando el modulo que servira ficheros estaticos
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
