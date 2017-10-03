from categories.models import Category
from ckeditor.fields import RichTextField
from django.db import models


# class AvailableManager(models.Manager):
#     def get_queryset(self):
#         return super(AvailableManager, self).get_queryset().filter(availability=True)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название товара', unique=True, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    category = models.ForeignKey(Category, verbose_name="Категория", related_name='products')
    article = models.CharField(max_length=50, blank=True, verbose_name='Артикул')

    short_description = RichTextField(blank=True, verbose_name='Краткое описание')
    description = RichTextField(blank=True, verbose_name='Полное описание')

    image = models.ImageField(upload_to='products/', blank=True, verbose_name='Главная картинка')
    weight = models.IntegerField(default=0, blank=True, verbose_name='Вес товара')

    available = models.BooleanField(default=True, verbose_name="Доступен для заказа")
    sort_weight = models.PositiveIntegerField(default=0, verbose_name='Вес для сортировки')

    created = models.DateTimeField(verbose_name="Дата добавления товара", auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения товара')

    # TODO: нужно добавить привязку товара к юзеру
    # owner = models.ForeignKey(User, related_name='products')

    # поле доступное через менеджер
    # https://djbook.ru/rel1.9/topics/db/managers.html
    # objects = models.Manager()
    # availabled = AvailableManager()

    def showimg(self):
        if self.image:
            return "<img src='{path}' style='max-height:100px;'>".format(path=self.image.url)
        else:
            return "no image"

    showimg.short_description = 'Изображение'
    showimg.allow_tags = True

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"
        ordering = ('-sort_weight', '-id')

        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name


class ProductAdditionalImage(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', related_name='ad_images')

    image = models.ImageField(upload_to='products/', blank=True, verbose_name='Дополнительная картинка товара')
    alt = models.CharField(max_length=100, blank=True, verbose_name='Alt текст изображения')

    created = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'


class ProductMeasure(models.Model):
    short = models.CharField(max_length=10, verbose_name='Краткое наименование', default='')
    full = models.CharField(max_length=50, verbose_name='Полное наименование', default='')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        return self.short


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, verbose_name='Цена', related_name='prices')

    description = models.CharField(max_length=100, verbose_name='Описание цены', blank=True)

    package_quantity = models.PositiveSmallIntegerField(default=1, verbose_name='Количество')
    measure = models.ForeignKey(ProductMeasure, verbose_name='Единица измерения')

    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return "{} {} руб.".format(self.description, self.price)
