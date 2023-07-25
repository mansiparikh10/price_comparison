from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse
from .models import AddItemForm
from .models import AddStoreItemForm, StoreItem
def index(request):
    store_items = StoreItem.objects.all()
    stores = StoreItem.objects.values('store_name', 'store_location').distinct()
    context = {
        'store_items': store_items,
        'stores': stores
    }
    return render(request, 'price_app/index.html', context)
def item(request): 
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddItemForm()

    return render(request, 'price_app/price.html', {'form': form})

def storeitem(request): 
    if request.method == 'POST':
        form = AddStoreItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddStoreItemForm()

    return render(request, 'price_app/storeprice.html', {'form': form})