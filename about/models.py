from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    descriptions = RichTextField()
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


