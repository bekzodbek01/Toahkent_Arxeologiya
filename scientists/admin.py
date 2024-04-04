from django.contrib import admin
from .models import Scientists


@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'create', 'update',)
    fields = ('fullname_uz', 'fullname_ru', 'fullname_en', 'descriptions_uz', 'descriptions_ru', 'descriptions_en',
              'position_uz', 'position_ru', 'position_en', 'image',)
