from django.db import models

# Create your models here.
class Publications(models.Model):
    title = models.TextField()
    image = models.ImageField()
    text = models.TextField()