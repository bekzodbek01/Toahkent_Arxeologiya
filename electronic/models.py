from django.db import models


class Electronic(models.Model):
    title = models.CharField(max_length=60)
    book = models.FileField(upload_to='book')


