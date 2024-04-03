from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    descriptions = models.TextField()
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)


class Archaeology(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    descriptions = RichTextField()
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Items(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
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
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
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


class Electronic(models.Model):
    title = models.CharField(max_length=60)
    book = models.FileField(upload_to='book')


