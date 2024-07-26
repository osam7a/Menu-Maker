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
        image_url = row.get('image_url')
        if image_url:
            response = requests.get(image_url)
            if response.status_code == 200:
                file_name = image_url.split('/')[-1]
                file_content = response.content
                file = File(file_content, name=file_name)
                row['image'] = file
        # Exclude the 'id' field from import
        row.pop('id', None)

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

    def before_import_row(self, row, **kwargs):
        image_url = row.get('image_url')
        if image_url:
            response = requests.get(image_url)
            if response.status_code == 200:
                file_name = image_url.split('/')[-1]
                file_content = response.content
                file = File(file_content, name=file_name)
                row['image'] = file
        # Exclude the 'id' field from import
        row.pop('id', None)

class ItemAdmin(ImportExportModelAdmin, TranslationAdmin):
    resource_class = ItemResource

class CategoryAdmin(ImportExportModelAdmin, TranslationAdmin):
    resource_class = CategoryResource

# Register your models here.
admin.site.register(Menu)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
