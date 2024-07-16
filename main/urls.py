from django.urls import path

from . import views

urlpatterns = [
    path('menu/<int:menu_id>/', views.menu, name='menu'),
]