from rest_framework import serializers
from .models import StoreItem, Store

class StoreItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoreItem
        fields = ['store_name', 'store_location','store_zipcode', 'item_name', 'item_category', 'item_brand', 'item_price','item_quantity', 'item_measure', 'added_on']

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'location','zipcode']