from django.db import models
from django.utils.translation import gettext as _

LABEL_COLORS = [
    ('red', _('Red')),
    ('blue', _('Blue')),
    ('green', _('Green')),
    ('yellow', _('Yellow'))
]

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=100)
    resturaunt_name = models.CharField(default="Resturaunt", max_length=100)
    logo = models.ImageField(upload_to='static/uploads/')
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    maps_link = models.CharField(blank=True, max_length=100)

    currency = models.CharField(max_length=10, default='EUR')
    template = models.CharField(max_length=100, default='basic')
    languages_allowed = models.ManyToManyField('Language')

    def __str__(self):
        return self.title_en + " | " + self.title_ar
    
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title + " | " + self.title_ar
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.TextField(blank=True)
    image = models.ImageField(upload_to='static/uploads/')

    featured = models.BooleanField(default=False)
    featured_label = models.CharField(max_length=100, blank=True)
    featured_label_color = models.CharField(max_length=100, blank=True, choices=LABEL_COLORS, default='red')

    def __str__(self):
        return self.title + " | " + self.title_ar
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

class Language(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    rtl = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
