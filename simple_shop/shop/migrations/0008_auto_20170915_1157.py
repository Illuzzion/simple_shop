# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20170915_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAdditionalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/', verbose_name='Дополнительная картинка товара')),
                ('alt', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name_plural': 'Изображения товара',
                'verbose_name': 'Изображение товара',
            },
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('weight', 'id'), 'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('weight', 'id'), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='categories/', verbose_name='Изображение для категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='seo_description',
            field=models.CharField(blank=True, max_length=100, verbose_name='Описание для SEO'),
        ),
        migrations.AddField(
            model_name='category',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ключевые слова для SEO'),
        ),
        migrations.AddField(
            model_name='category',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Вес для сортировки'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/', verbose_name='Главная картинка товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Вес для сортировки'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступен к заказу'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения товара'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.AddField(
            model_name='productadditionalimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Товар'),
        ),
    ]
