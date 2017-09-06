from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория товара', unique=True)
    slug = models.SlugField(max_length=150)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = "Категории товаров"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара', unique=True)
    category = models.ForeignKey(ProductCategory)
    slug = models.SlugField(max_length=150)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"
        ordering = ('name',)

    def __str__(self):
        return self.name
