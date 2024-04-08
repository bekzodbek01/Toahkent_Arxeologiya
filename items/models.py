from django.db import models
from ckeditor.fields import RichTextField

class Items(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    descriptions = RichTextField()
    downloads = models.IntegerField(default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title