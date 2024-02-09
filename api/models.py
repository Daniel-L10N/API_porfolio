from django.db import models

# Create your models here.
class Programer(models.Model):
    fullname = models.CharField(max_length = 100)
    nickname = models.CharField(max_length = 50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default = True)
    
    def __str__(self):
        if self.is_active: active  = "Activo"
        else:active = "no activo"
        return f"{self.nickname} programador {active}"