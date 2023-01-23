from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def cards_cow(request):
    return render(request, 'main/card_prod_cow.html')

def cards_pig(request):
    return render(request, 'main/card_prod_pig.html')

def cards_chic(request):
    return render(request, 'main/card_prod_chicken.html')