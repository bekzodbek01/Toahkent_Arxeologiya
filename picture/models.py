from django.db import models


class Picture(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return self.title
