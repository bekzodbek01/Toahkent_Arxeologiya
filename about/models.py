from django.db import models


class About(models.Model):
    descriptions = models.TextField()
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)

