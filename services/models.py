from django.db import models

""" 
    mapeado (ORM) (modelo objeto relacional) se puede trabajar con objetos mapeados en la base de datos
    de manera que si se crean instanicas de una clase especifica estas se quedan guardadas como registros 
    de forma automatica, cuando las recuperemos y las modifiquemos los valores tambien qudaran guardados en l
    base de datos.
"""

# Al emlasar los modelos con la base de datos se tiene que segir normas de las bases de datos como el (max_leght)
# Creando un nuevo modelo (heredando de model.Model) 'eta clase repesenta una tabla dentro de la base de datos'
# la tablas estan formadas por columnas y cada fila representara un registro (cada atributo de esta clase represetare una de esas columnas)
class Service(models.Model):
    #  se debe indicar lo modelos definidos que representaran esos campos (cadena textos,img,stc)
    # algunos de estos requieren atributos para poder funcionar como (charfield(max_lenght))
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="Contenido")
    # upload_to : indica todos las imagenes lo suban al media pero dentro de una carpeta Services
    image = models.ImageField(verbose_name="Imagen", upload_to="Services")
    # auto_now_add (se añadira automticamente la hora cunado se cree por primera vez,'funciona solo una vez')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    # auto_now ( se añadira automaticamenta la hora cuando se actualize 'funciona siempre')
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    
    # para poder añadir metadatos extendidos
    class Meta:
        # definimos el nombre em expañol
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        # campo de ordenacio por defecto (por defecto de mas antiguo a mas nuevo) el (-) invierte este orden
        ordering = ['-created']

    # metodo para poder visualizar el nombre de los proyectos en el administrdor
    def __str__(self):
        return self.title
