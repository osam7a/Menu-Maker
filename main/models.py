from django.db import models
from django.utils.translation import gettext as _

from os import listdir, path

LABEL_COLORS = [
    ('red', _('Red')),
    ('blue', _('Blue')),
    ('green', _('Green')),
    ('yellow', _('Yellow'))
]

TEMPLATES = []
for template in listdir("templates"):
    if path.isdir('templates/' + template):
        TEMPLATES.append((template, template))

class Thumbnail(models.Model):
    file = models.ImageField(blank=True, upload_to='static/uploads/', help_text=_("The thumbnail image."))

class Menu(models.Model):
    title = models.CharField(max_length=100, help_text=_("The title of the menu."))
    resturaunt_name = models.CharField(default="Resturaunt", max_length=100, help_text=_("The name of the restaurant."))
    logo = models.ImageField(upload_to='static/uploads/', help_text=_("The logo image of the menu."))
    address = models.CharField(max_length=100, help_text=_("The address of the restaurant."))
    phone = models.CharField(max_length=100, help_text=_("The phone number of the restaurant."))
    maps_link = models.CharField(blank=True, max_length=100, help_text=_("The link to the restaurant's location on maps."))

    currency = models.CharField(max_length=10, default='EUR', help_text=_("The currency used for pricing."))
    template = models.CharField(max_length=100, default='basic', help_text=_("The template used for the menu."), choices=TEMPLATES)
    thumbnails = models.ManyToManyField(Thumbnail, blank=True)

    languages_allowed = models.ManyToManyField('Language', help_text=_("The languages allowed for the menu."))

    def __str__(self):
        return "#" + str(self.id) + " " + self.title
    
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, help_text=_("The menu that the category belongs to."))
    title = models.CharField(max_length=100, help_text=_("The title of the category."))

    def __str__(self):
        return "#" + str(self.id) + " " + self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, help_text=_("The menu that the item belongs to."))
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, help_text=_("The category that the item belongs to."))

    title = models.CharField(max_length=100, help_text=_("The title of the item."))
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text=_("The price of the item."))
    compare_at_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text=_("Do you want to do a sale? This will be the price before discount."))
    ingredients = models.TextField(blank=True, help_text=_("The ingredients of the item."))
    image = models.ImageField(blank=True, upload_to='static/uploads/', help_text=_("The image of the item."))

    group = models.BooleanField(default=False, help_text=_("Is this item suitable for more than 1 person?"))
    vegan = models.BooleanField(default=False, help_text=_("Can this item be eaten by vegeterians?"))
    combo = models.BooleanField(default=False, help_text=_("Does the item come with a side & drink?"))

    def __str__(self):
        return "#" + str(self.id) + " " + self.title
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

class Language(models.Model):
    code = models.CharField(max_length=2, help_text=_("The code of the language."))
    name = models.CharField(max_length=100, help_text=_("The name of the language."))
    rtl = models.BooleanField(default=False, help_text=_("Whether the language is right-to-left."))

    def __str__(self):
        return "#" + str(self.id) + " " + self.name

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
