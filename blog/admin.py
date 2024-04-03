from django.contrib import admin
from .models import About, Archaeology, Items, Scientists, Video, Picture, News, Electronic
# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('descriptions',)
    fields = ('descriptions_uz', 'descriptions_ru', 'descriptions_en', 'video', 'link',)


@admin.register(Archaeology)
class ArchaeologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update',)
    fields = ('descriptions_uz', 'descriptions_ru', 'descriptions_en', 'title_uz', 'title_ru',
              'title_en', 'video', 'link', 'image',)


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update',)
    fields = ('descriptions_uz', 'descriptions_ru', 'descriptions_en', 'title_uz', 'title_ru',
              'title_en', 'video', 'link', 'image',)


@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'create', 'update',)
    fields = ('fullname_uz', 'fullname_ru', 'fullname_en', 'descriptions_uz', 'descriptions_ru', 'descriptions_en',
              'position_uz', 'position_ru', 'position_en', 'image',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'video', 'link',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'image',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update',)
    fields = ('title_uz', 'title_ru', 'title_en', 'descriptions_uz', 'descriptions_ru', 'descriptions_en', 'image',)


@admin.register(Electronic)
class ElectronicAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'book',)


