from django.shortcuts import render, get_object_or_404

from .models import Menu, Category, Item

# Create your views here.
def menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    categories = Category.objects.filter(menu=menu)
    thumbnails = menu.thumbnails
    # sort category items by compare_at_price

    context = {
        'menu': menu,
        'categories': categories,
        'thumbnails': thumbnails.all()
    }

    if not request.GET.get('selected'):
        return render(request, menu.template + '/menu-selector.html', context)
    else:
        return render(request, menu.template + '/menu.html', context)