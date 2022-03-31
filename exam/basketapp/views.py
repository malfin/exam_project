from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Products


def basket(request):
    product = Basket.objects.filter(user=request.user)
    context = {
        'title': 'корзина',
        'product': product,
    }
    return render(request, 'basketapp/index.html', context)


def add_to_card(request, pk):
    product = Products.objects.get(id=pk)
    card_object, created = Basket.objects.get_or_create(
        user=request.user,
        products=product,
    )
    if created:
        print('Вы добавили товар')
        HttpResponseRedirect(reverse('mainapp:select_product', kwargs={'select_product': pk}))
    print('Товар уже в корзине!')
