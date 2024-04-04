from django.contrib import admin
from video.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'video', 'link',)

