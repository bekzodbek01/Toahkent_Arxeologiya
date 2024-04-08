from django.db import models


class Electronic(models.Model):
    title = models.CharField(max_length=60)
    book = models.FileField(upload_to='book')

    class Meta:
        verbose_name = 'Electronic'
        verbose_name_plural = 'Electronics'

    def __str__(self):
        return self.title


