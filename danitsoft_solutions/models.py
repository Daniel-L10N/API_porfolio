from django.db import models
import os

# Create your models here.
class Incentive(models.Model):
    title= models.CharField(max_length = 60)
    description = models.CharField(max_length = 200)
    image= models.ImageField(upload_to='media/incentive')

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super(Incentive, self).delete(*args, **kwargs)


    def __str__(self):
        return self.title
