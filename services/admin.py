from django.contrib import admin
# importando el modelo Services para poder tenerlo en el admin de django
from .models import Service


# Register your models here.

# Creando una condiguracion extendida basica para le administrador
class ServiceAdmin(admin.ModelAdmin):
    # esto re ulitiza para mostrat los campos que son de solo lectura en el panel del administrador
    readonly_fields = ('created', 'updated')

# registrando el servicio y su configuracion extendida 
admin.site.register(Service,ServiceAdmin)