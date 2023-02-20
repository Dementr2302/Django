from django.shortcuts import render ,HttpResponseRedirect
from django.http import HttpResponse
from main.models import ProductCategory, Product
from main.models import Basket
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'main/index.html')

def cards_cow(request):
    context = {
        'h1': 'Говядина',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'main/card_prod_cow.html', context)

def cards_pig(request):
    context = {
        'h1': 'Свинина',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'main/card_prod_pig.html', context)

def cards_chic(request):
    context = {
        'h1': 'Курятина',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'main/card_prod_chicken.html', context)

@login_required
def basket_add(requset, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=requset.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=requset.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(requset.META['HTTP_REFERER'])
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])