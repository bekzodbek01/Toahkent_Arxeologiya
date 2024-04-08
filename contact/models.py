from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    description = RichTextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.full_name

