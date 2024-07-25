from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static

from .models import Menu, Category, Item

# Create your views here.
def menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    categories = Category.objects.filter(menu=menu)
    items = Item.objects.filter(menu=menu)

    context = {
        'menu': menu,
        'categories': categories,
        'items': items,
    }

    if not request.GET.get('selected'):
        return render(request, menu.template + '/menu-selector.html', context)
    else:
        return render(request, menu.template + '/menu.html', context)