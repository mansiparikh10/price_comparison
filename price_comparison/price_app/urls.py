from django.urls import path
from .  import views
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'StoreItem', views.StoreItemViewSet)
router.register(r'Store', views.StoreViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('price', views.item, name='item'),
    path('storeprice', views.storeitem, name='storeitem'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]