# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-18 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_report_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='bill_image',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_time',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_datetime',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='total_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
