from django.db import models
from django.forms import ModelForm
class User(models.Model):
    userid = models.CharField(max_length=32)
    password = models.CharField(max_length=16)

class Store(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=256)
    zipcode = models.IntegerField()

class Item(models.Model):
    ITEM_MEASURES = (
        ('KG', 'Kilogram'),
        ('LB', 'Pound'),
        ('OZ', 'Ounce'),
        ('GMS', 'Gram'),
        ('EA', 'Each')
    )

    item_name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    measure = models.CharField(max_length=3, null=True, choices=ITEM_MEASURES)
class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'category', 'brand', 'price','quantity', 'measure']

class StoreItem(models.Model):
    STOREITEM_MEASURES = (
        ('KG', 'Kilogram'),
        ('LB', 'Pound'),
        ('OZ', 'Ounce'),
        ('GMS', 'Gram'),
        ('EA', 'Each')
    )
    store_name = models.CharField(max_length=64)
    store_location = models.CharField(max_length=256)
    store_zipcode = models.IntegerField()
    item_name = models.CharField(max_length=64)
    item_category = models.CharField(max_length=64)
    item_brand = models.CharField(max_length=64)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_quantity = models.IntegerField()
    item_measure = models.CharField(max_length=3, null=True, choices=STOREITEM_MEASURES)
    added_on = models.DateTimeField()
class AddStoreItemForm(ModelForm):
    class Meta:
        model = StoreItem
        fields = ['store_name', 'store_location','store_zipcode', 'item_name', 'item_category', 'item_brand', 'item_price','item_quantity', 'item_measure', 'added_on']