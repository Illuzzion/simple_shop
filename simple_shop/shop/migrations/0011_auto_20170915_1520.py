# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20170915_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
        ),
        migrations.AlterField(
            model_name='productprice',
            name='measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ProductMeasure', verbose_name='Единица измерения'),
        ),
    ]