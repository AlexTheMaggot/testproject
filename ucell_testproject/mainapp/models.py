from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    color = models.CharField(max_length=200, verbose_name='Цвет')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
