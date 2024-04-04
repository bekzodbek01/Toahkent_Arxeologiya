from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    descriptions = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)