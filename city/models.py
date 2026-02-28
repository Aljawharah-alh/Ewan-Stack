from django.db import models

# Create your models here.

class City(models.Model):
    name=models.CharField(max_length=50)
    image_url = models.URLField(max_length=500, default='')
    def __str__(self):
        return self.name