from django.db import models


class Video(models.Model):
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    title = models.CharField(max_length=60)

