from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from mainapp.models import Products


def index(request):
    order_type = 'year_of_issue'
    if 'places_order_type' in request.session.keys():
        order_type = request.session['places_order_type']
        print(f'выбрана сортировка: {order_type}')
    products = Products.objects.filter(in_stock=True).order_by(order_type)
    context = {
        'title': 'Каталог',
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def places_order_set(request, order_type):
    request.session['places_order_type'] = order_type
    print(order_type)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def select_product(request, pk):
    products = get_object_or_404(Products, id=pk)
    context = {
        'title': products.name,
        'products': products,
    }
    return render(request, 'mainapp/select_product.html', context)


def about(request):
    products = Products.objects.filter(in_stock=True)[0:5]
    context = {
        'title': 'О нас',
        'products': products,
    }
    return render(request, 'mainapp/about.html', context)


def find(request):
    context = {
        'title': 'где нас найти?',
    }
    return render(request, 'mainapp/find.html', context)
