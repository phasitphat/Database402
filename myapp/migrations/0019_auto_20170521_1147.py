# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-21 04:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_productinorder_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='status',
            new_name='status_order',
        ),
    ]
