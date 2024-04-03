from modeltranslation.translator import TranslationOptions, register

from blog.models import About, Archaeology, Items, Scientists, Video, Picture, News, Electronic


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('descriptions',)


@register(Archaeology)
class ArchaeologyTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Items)
class ItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Scientists)
class ScientistsTranslationOptions(TranslationOptions):
    fields = ('fullname', 'position', 'descriptions',)


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Picture)
class PictureTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Electronic)
class ElectronicTranslationOptions(TranslationOptions):
    fields = ('title',)

