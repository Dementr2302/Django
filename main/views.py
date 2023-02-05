from django.shortcuts import render
from django.http import HttpResponse
from main.models import ProductCategory, Product


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