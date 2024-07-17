from django.db import models

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

    def __str__(self):
        return self.title

class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title