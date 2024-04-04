from modeltranslation.translator import TranslationOptions, register
from .models import Scientists


@register(Scientists)
class ScientistsTranslationOptions(TranslationOptions):
    fields = ('fullname', 'position', 'descriptions',)