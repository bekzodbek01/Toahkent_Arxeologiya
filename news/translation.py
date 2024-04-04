from modeltranslation.translator import TranslationOptions, register
from news.models import News


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)

