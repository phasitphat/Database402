# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-12 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20170512_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='productinorder_id',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='totalprice_per_product',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]