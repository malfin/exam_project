from django.urls import path, re_path

app_name = 'mainapp'

import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('about/', mainapp.about, name='about'),
    path('find/', mainapp.find, name='find'),
    path('select-products/<int:pk>/', mainapp.select_product, name='select_product'),

    re_path(r'^order/set/(-*\w+)/$', mainapp.places_order_set, name='places_order_set')
    # re_path('^places/order/set/(\-*\w+)/$', mainapp.places_order_set, name='places_order_set'),

    # re_path('^places/order/set/()/', mainapp.places_order_set, name='places_order_set'),
]
