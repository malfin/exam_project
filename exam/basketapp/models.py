from django.db import models

from authapp.models import KpkUser
from mainapp.models import Products


class Basket(models.Model):
    user = models.ForeignKey(KpkUser, on_delete=models.CASCADE, verbose_name='пользователь')
    products = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='товар')
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.login

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзин'
