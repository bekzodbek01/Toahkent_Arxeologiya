from django.contrib import admin
from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update',)
    fields = ('title_uz', 'title_ru', 'title_en', 'descriptions_uz', 'descriptions_ru', 'descriptions_en', 'image',)

