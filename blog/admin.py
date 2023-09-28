from django.contrib import admin
# importando el modelo Post para poder tenerlo en el admin de django
from .models import Post

# Register your models here.

# Creando una condiguracion extendida basica para le administrador
class PostAdmin(admin.ModelAdmin):
    # esto re ulitiza para mostrat los campos que son de solo lectura en el panel del administrador
    readonly_fields = ('created', 'updated')



admin.site.register(Post, PostAdmin)