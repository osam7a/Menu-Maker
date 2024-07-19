from modeltranslation.translator import TranslationOptions, register

from main.models import Item, Category, Menu

@register(Item)
class ItemTranslationOptions(TranslationOptions):
    fields = ('title', 'ingredients')
    required_languages = ('en',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('en',)

@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'address')
    required_languages = ('en',)
