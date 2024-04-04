from modeltranslation.translator import TranslationOptions, register
from items.models import Items


@register(Items)
class ItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)