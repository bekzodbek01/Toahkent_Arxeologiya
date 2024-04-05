from django.db import models
from ckeditor.fields import RichTextField


class Scientists(models.Model):
    fullname = models.CharField(max_length=100)
    position = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images')
    descriptions = RichTextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
