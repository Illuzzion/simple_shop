from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=150, verbose_name='Название категории', unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            verbose_name='Родительская категория')

    description = models.TextField(verbose_name='Описание категории', blank=True)
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение для категории', blank=True)
    sort_weight = models.PositiveIntegerField(default=0, verbose_name='Вес для сортировки')

    seo_keywords = models.CharField(max_length=100, verbose_name='Ключевые слова для SEO', blank=True)
    seo_description = models.CharField(max_length=100, verbose_name='Описание для SEO', blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = "Категории товаров"
        ordering = ('-sort_weight', 'id')

    def __str__(self):
        return self.name
