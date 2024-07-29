import requests
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TranslationAdmin

from django.contrib import admin
from django.core.files import File

from .models import *

class ItemResource(resources.ModelResource):
    class Meta:
        model = Item

    def before_import_row(self, row, **kwargs):
        row.pop('image', None)
        row.pop('id', None)

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

    def before_import_row(self, row, **kwargs):
        # Exclude the 'id' field from import
        row.pop('id', None)

class ItemAdmin(ImportExportModelAdmin, TranslationAdmin):
    resource_class = ItemResource

class CategoryAdmin(ImportExportModelAdmin, TranslationAdmin):
    resource_class = CategoryResource

# Register your models here.
admin.site.register(Menu)
admin.site.register(Thumbnail)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
