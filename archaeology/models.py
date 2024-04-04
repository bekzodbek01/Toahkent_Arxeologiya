from django.db import models
from ckeditor.fields import RichTextField


class Archaeology(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    descriptions = RichTextField()
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)