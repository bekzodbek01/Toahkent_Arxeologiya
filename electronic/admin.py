from django.contrib import admin
from electronic.models import Electronic


@admin.register(Electronic)
class ElectronicAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'book',)


