from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLogForm, UserRegForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse
from main.models import Basket
def login(request):
    if request.method =='POST':                         #КОНТРОЛЬ // проверка на пост запрос
        form = UserLogForm(data=request.POST)           # вызываем класс , передавая параметр - данные которые были заполнены в форме
        if form.is_valid():                             # проверка на валидность
            username = request.POST['username']         # достаем данные username
            password = request.POST['password']         # достаем данные password
            user = auth.authenticate(username=username,password=password)       # ПОДТВЕРЖДЕНИЕ ПОДЛИННОСТИ // проверка есть ли пользователь
            if user:                                    # если он(пользователь) есть
                auth.login(request, user)               # мы его авторизовали  // РАЗРЕШЕНИЕ
                return HttpResponseRedirect('/')     # немного не правильно надо бы на url исправить // пернаправляем на главную страницу
    else:
        form = UserLogForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)

    context = {'title': "Meet - Profil",
               'form': form,
               'baskets': baskets,
               'total_sum': total_sum,
               'total_quantity': total_quantity,
               }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))

