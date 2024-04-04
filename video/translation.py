from modeltranslation.translator import TranslationOptions, register
from video.models import Video

@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)

