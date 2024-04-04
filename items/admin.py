from django.contrib import admin
from items.models import Items


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update',)
    fields = ('descriptions_uz', 'descriptions_ru', 'descriptions_en', 'title_uz', 'title_ru',
              'title_en', 'video', 'link', 'image',)
