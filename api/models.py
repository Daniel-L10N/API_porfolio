from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

class Programer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='media/programers')

# Señal para manejar la eliminación de la imagen antes de que se elimine el objeto
@receiver(pre_delete, sender=Programer)
def delete_image(sender, instance, **kwargs):
    # Elimina la imagen del almacenamiento si existe
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


# from django.db import models
# from django.db.models.signals import pre_delete
# import os

# class Programer(models.Model):
#     fullname = models.CharField(max_length=100)
#     nickname = models.CharField(max_length=50)
#     age = models.PositiveSmallIntegerField()
#     image = models.ImageField(upload_to='media/programers')

    

#     def delete(self, *args, **kwargs):
#         # Verificar si self.image existe para manejar el caso null=True
#         if self.image and os.path.isfile(self.image.path):
#             os.remove(self.image.path)
#         super().delete(**kwargs)

#     def __str__(self):
#         return self.nickname
