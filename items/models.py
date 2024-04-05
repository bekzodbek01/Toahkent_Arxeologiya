from django.db import models


class Items(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    descriptions = models.TextField()
    downloads = models.IntegerField(default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)