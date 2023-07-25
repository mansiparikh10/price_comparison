from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('price', views.item, name='item'),
    path('storeprice', views.storeitem, name='storeitem'),
]