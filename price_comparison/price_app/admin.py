from django.contrib import admin
from .models import User
from .models import Store
from .models import Item
from .models import StoreItem
admin.site.register(User)
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(StoreItem)