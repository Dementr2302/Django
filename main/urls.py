from django.urls import path
from . import views
from main.views import basket_add, basket_remove

urlpatterns = [
    path('', views.index, name='home'),
    path('cards_cow', views.cards_cow, name='cow'),
    path('cards_pig', views.cards_pig, name='pig'),
    path('cards_chic', views.cards_chic, name='chicken'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
