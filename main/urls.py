
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('cards_cow', views.cards_cow, name='cow'),
    path('cards_pig', views.cards_pig, name='pig'),
    path('cards_chic', views.cards_chic, name='chicken'),


]