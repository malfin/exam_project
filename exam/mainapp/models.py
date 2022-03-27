from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название товара', max_length=128)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name='изображение', upload_to=f'products/{name}/')
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
