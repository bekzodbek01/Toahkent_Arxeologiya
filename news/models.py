from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)
    descriptions = RichTextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title