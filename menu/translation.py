from .models import MenuItem, Menu
from modeltranslation.translator import register, TranslationOptions


@register(MenuItem)
class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title',)
