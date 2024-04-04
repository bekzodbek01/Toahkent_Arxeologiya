from django.contrib import admin
from .models import Archaeology


@admin.register(Archaeology)
class ArchaeologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update',)
    fields = ('descriptions_uz', 'descriptions_ru', 'descriptions_en', 'title_uz', 'title_ru',
              'title_en', 'video', 'link', 'image',)
