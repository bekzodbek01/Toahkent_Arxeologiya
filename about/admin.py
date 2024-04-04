from django.contrib import admin
from about.models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('descriptions',)
    fields = ('descriptions_uz', 'descriptions_ru', 'descriptions_en', 'video', 'link',)