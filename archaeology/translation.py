from modeltranslation.translator import TranslationOptions, register
from archaeology.models import Archaeology


@register(Archaeology)
class ArchaeologyTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


