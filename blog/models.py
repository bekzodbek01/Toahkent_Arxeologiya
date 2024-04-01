from django.db import models
from ckeditor.fields import RichTextField



class About(models.Model):
    descriptions = models.TextField()
    video = models.FileField(upload_to='video')


class Archaeology(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    descriptions = RichTextField()
    video = models.FileField(upload_to='video')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Items(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    video = models.FileField(upload_to='video')
    descriptions = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Scientists(models.Model):
    fullname = models.CharField(max_length=100)
    position = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images')
    descriptions = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Video(models.Model):
    video = models.FileField(upload_to='video')
    title = models.CharField(max_length=60)


class Picture(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)



class News(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    descriptions = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)



class electronic(models.Model):
    title = models.CharField(max_length=60)
    book = models.FileField(upload_to='book')


