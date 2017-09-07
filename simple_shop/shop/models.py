from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория товара', unique=True)
    slug = models.SlugField(max_length=150)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = "Категории товаров"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория")  # related_name='products'

    name = models.CharField(max_length=150, verbose_name='Название товара', unique=True, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)

    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products/', blank=True, verbose_name='Картинка товара')

    available = models.BooleanField(default=True, verbose_name="На витрине")

    created = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"
        ordering = ('-id',)  # порядок сортировки по умолчанию
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name
