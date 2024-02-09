from django.db import models

# Create your models here.
class Programer(models.Model):
    fullname = models.CharField(max_length = 100)
    nickname = models.CharField(max_length = 50)
    age = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='media/programers', null=True)
    
    def __str__(self):
        return self.nickname