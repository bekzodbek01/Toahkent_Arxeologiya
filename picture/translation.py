from modeltranslation.translator import TranslationOptions, register
from picture.models import Picture


@register(Picture)
class PictureTranslationOptions(TranslationOptions):
    fields = ('title',)
