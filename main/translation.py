from modeltranslation.translator import TranslationOptions, register

from main.models import Item, Category, Menu

@register(Item)
class ItemTranslationOptions(TranslationOptions):
    fields = ('title', 'ingredients')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'address')
