from django.contrib import admin

from mainapp.models import Products, Category

admin.site.register(Category)
admin.site.register(Products)
