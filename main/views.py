from django.shortcuts import render
from django.templatetags.static import static

# Create your views here.
def menu(request, menu_id):
    return render(request, 'menu.html')