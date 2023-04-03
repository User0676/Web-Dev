from django.db import models


class Product(models.Model):
    name = models.CharField('name',max_length=50)
    price = models.FloatField('price')
    description = models.TextField('description')
    count = models.IntegerField('count')
    is_active = models.BooleanField('status')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'


class Category(models.Model):
    name = models.CharField('name',max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

