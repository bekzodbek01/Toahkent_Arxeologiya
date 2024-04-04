from modeltranslation.translator import TranslationOptions, register
from electronic.models import Electronic


@register(Electronic)
class ElectronicTranslationOptions(TranslationOptions):
    fields = ('title',)

