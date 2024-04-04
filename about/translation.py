from modeltranslation.translator import TranslationOptions, register
from about.models import About


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('descriptions',)

