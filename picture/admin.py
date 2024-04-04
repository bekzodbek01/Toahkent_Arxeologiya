from django.contrib import admin
from picture.models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'image',)

