# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-12 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
