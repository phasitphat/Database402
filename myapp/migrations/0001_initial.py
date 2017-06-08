# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-09 03:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('category_detail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_age', models.CharField(blank=True, max_length=2, null=True)),
                ('customer_gender', models.CharField(blank=True, choices=[('1', '\u0e40\u0e1e\u0e28\u0e0a\u0e32\u0e22'), ('2', '\u0e40\u0e1e\u0e28\u0e2b\u0e0d\u0e34\u0e07')], max_length=6, null=True)),
                ('customer_job', models.CharField(blank=True, choices=[('1', '\u0e19\u0e31\u0e01\u0e40\u0e23\u0e35\u0e22\u0e19/\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32'), ('2', '\u0e04\u0e23\u0e39/\u0e2d\u0e32\u0e08\u0e32\u0e23\u0e22\u0e4c'), ('3', '\u0e41\u0e1e\u0e17\u0e22\u0e4c/\u0e1e\u0e22\u0e32\u0e1a\u0e32\u0e25'), ('4', '\u0e17\u0e2b\u0e32\u0e23/\u0e15\u0e33\u0e23\u0e27\u0e08'), ('5', '\u0e23\u0e31\u0e1a\u0e08\u0e49\u0e32\u0e07'), ('6', '\u0e1e\u0e19\u0e31\u0e01\u0e07\u0e32\u0e19\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17'), ('7', '\u0e02\u0e49\u0e32\u0e23\u0e32\u0e0a\u0e01\u0e32\u0e23'), ('8', '\u0e40\u0e01\u0e29\u0e15\u0e23\u0e01\u0e23'), ('9', '\u0e19\u0e31\u0e01\u0e01\u0e0e\u0e2b\u0e21\u0e32\u0e22'), ('10', '\u0e19\u0e31\u0e01\u0e01\u0e32\u0e23\u0e40\u0e21\u0e37\u0e2d\u0e07'), ('11', '\u0e19\u0e31\u0e01\u0e27\u0e34\u0e17\u0e22\u0e32\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('12', '\u0e28\u0e34\u0e25\u0e1b\u0e34\u0e19'), ('13', '\u0e40\u0e0a\u0e1f'), ('14', '\u0e2d\u0e37\u0e48\u0e19 \u0e46')], max_length=100, null=True)),
                ('customer_province', models.CharField(blank=True, choices=[('1', '\u0e01\u0e23\u0e38\u0e07\u0e40\u0e17\u0e1e\u0e21\u0e2b\u0e32\u0e19\u0e04\u0e23'), ('2', '\u0e01\u0e23\u0e30\u0e1a\u0e35\u0e48'), ('3', '\u0e01\u0e32\u0e0d\u0e08\u0e19\u0e1a\u0e38\u0e23\u0e35'), ('4', '\u0e01\u0e32\u0e2c\u0e2a\u0e34\u0e19\u0e18\u0e38\u0e4c'), ('5', '\u0e01\u0e33\u0e41\u0e1e\u0e07\u0e40\u0e1e\u0e0a\u0e23'), ('6', '\u0e02\u0e2d\u0e19\u0e41\u0e01\u0e48\u0e19'), ('7', '\u0e08\u0e31\u0e19\u0e17\u0e1a\u0e38\u0e23\u0e35'), ('8', '\u0e09\u0e30\u0e40\u0e0a\u0e34\u0e07\u0e40\u0e17\u0e23\u0e32'), ('9', '\u0e0a\u0e25\u0e1a\u0e38\u0e23\u0e35'), ('10', '\u0e0a\u0e31\u0e22\u0e19\u0e32\u0e17'), ('11', '\u0e0a\u0e31\u0e22\u0e20\u0e39\u0e21\u0e34'), ('12', '\u0e0a\u0e38\u0e21\u0e1e\u0e23'), ('13', '\u0e40\u0e0a\u0e35\u0e22\u0e07\u0e23\u0e32\u0e22'), ('14', '\u0e40\u0e0a\u0e35\u0e22\u0e07\u0e43\u0e2b\u0e21\u0e48'), ('15', '\u0e15\u0e23\u0e31\u0e07'), ('16', '\u0e15\u0e23\u0e32\u0e14'), ('17', '\u0e15\u0e32\u0e01'), ('18', '\u0e19\u0e04\u0e23\u0e19\u0e32\u0e22\u0e01'), ('19', '\u0e19\u0e04\u0e23\u0e1b\u0e10\u0e21'), ('20', '\u0e19\u0e04\u0e23\u0e1e\u0e19\u0e21'), ('21', '\u0e19\u0e04\u0e23\u0e23\u0e32\u0e0a\u0e2a\u0e35\u0e21\u0e32'), ('22', '\u0e19\u0e04\u0e23\u0e28\u0e23\u0e35\u0e18\u0e23\u0e23\u0e21\u0e23\u0e32\u0e0a'), ('23', '\u0e19\u0e04\u0e23\u0e2a\u0e27\u0e23\u0e23\u0e04\u0e4c'), ('24', '\u0e19\u0e19\u0e17\u0e1a\u0e38\u0e23\u0e35'), ('25', '\u0e19\u0e23\u0e32\u0e18\u0e34\u0e27\u0e32\u0e2a'), ('26', '\u0e19\u0e48\u0e32\u0e19'), ('27', '\u0e1a\u0e36\u0e07\u0e01\u0e32\u0e2c'), ('28', '\u0e1a\u0e38\u0e23\u0e35\u0e23\u0e31\u0e21\u0e22\u0e4c'), ('29', '\u0e1b\u0e17\u0e38\u0e21\u0e18\u0e32\u0e19\u0e35'), ('30', '\u0e1b\u0e23\u0e30\u0e08\u0e27\u0e1a\u0e04\u0e35\u0e23\u0e35\u0e02\u0e31\u0e19\u0e18\u0e4c'), ('31', '\u0e1b\u0e23\u0e32\u0e08\u0e35\u0e19\u0e1a\u0e38\u0e23\u0e35'), ('32', '\u0e1b\u0e31\u0e15\u0e15\u0e32\u0e19\u0e35'), ('33', '\u0e1e\u0e23\u0e30\u0e19\u0e04\u0e23\u0e28\u0e23\u0e35\u0e2d\u0e22\u0e38\u0e18\u0e22\u0e32'), ('34', '\u0e1e\u0e31\u0e07\u0e07\u0e32'), ('35', '\u0e1e\u0e31\u0e17\u0e25\u0e38\u0e07'), ('36', '\u0e1e\u0e34\u0e08\u0e34\u0e15\u0e23'), ('37', '\u0e1e\u0e34\u0e29\u0e13\u0e38\u0e42\u0e25\u0e01'), ('38', '\u0e40\u0e1e\u0e0a\u0e23\u0e1a\u0e38\u0e23\u0e35'), ('39', '\u0e40\u0e1e\u0e0a\u0e23\u0e1a\u0e39\u0e23\u0e13\u0e4c'), ('40', '\u0e41\u0e1e\u0e23\u0e48'), ('41', '\u0e1e\u0e30\u0e40\u0e22\u0e32'), ('42', '\u0e20\u0e39\u0e40\u0e01\u0e47\u0e15'), ('43', '\u0e21\u0e2b\u0e32\u0e2a\u0e32\u0e23\u0e04\u0e32\u0e21'), ('44', '\u0e21\u0e38\u0e01\u0e14\u0e32\u0e2b\u0e32\u0e23'), ('45', '\u0e41\u0e21\u0e48\u0e2e\u0e48\u0e2d\u0e07\u0e2a\u0e2d\u0e19'), ('46', '\u0e22\u0e30\u0e25\u0e32'), ('47', '\u0e22\u0e42\u0e2a\u0e18\u0e23'), ('48', '\u0e23\u0e49\u0e2d\u0e22\u0e40\u0e2d\u0e47\u0e14'), ('49', '\u0e23\u0e30\u0e19\u0e2d\u0e07'), ('50', '\u0e23\u0e30\u0e22\u0e2d\u0e07'), ('51', '\u0e23\u0e32\u0e0a\u0e1a\u0e38\u0e23\u0e35'), ('52', '\u0e25\u0e1e\u0e1a\u0e38\u0e23\u0e35'), ('53', '\u0e25\u0e33\u0e1b\u0e32\u0e07'), ('54', '\u0e25\u0e33\u0e1e\u0e39\u0e19'), ('55', '\u0e40\u0e25\u0e22'), ('56', '\u0e28\u0e23\u0e35\u0e2a\u0e30\u0e40\u0e01\u0e29'), ('57', '\u0e2a\u0e01\u0e25\u0e19\u0e04\u0e23'), ('58', '\u0e2a\u0e07\u0e02\u0e25\u0e32'), ('59', '\u0e2a\u0e15\u0e39\u0e25'), ('60', '\u0e2a\u0e21\u0e38\u0e17\u0e23\u0e1b\u0e23\u0e32\u0e01\u0e32\u0e23'), ('61', '\u0e2a\u0e21\u0e38\u0e17\u0e23\u0e2a\u0e07\u0e04\u0e23\u0e32\u0e21'), ('62', '\u0e2a\u0e21\u0e38\u0e17\u0e23\u0e2a\u0e32\u0e04\u0e23'), ('63', '\u0e2a\u0e23\u0e30\u0e41\u0e01\u0e49\u0e27'), ('64', '\u0e2a\u0e23\u0e30\u0e1a\u0e38\u0e23\u0e35'), ('65', '\u0e2a\u0e34\u0e07\u0e2b\u0e4c\u0e1a\u0e38\u0e23\u0e35'), ('66', '\u0e2a\u0e38\u0e42\u0e02\u0e17\u0e31\u0e22'), ('67', '\u0e2a\u0e38\u0e1e\u0e23\u0e23\u0e13\u0e1a\u0e38\u0e23\u0e35'), ('68', '\u0e2a\u0e38\u0e23\u0e32\u0e29\u0e0e\u0e23\u0e4c\u0e18\u0e32\u0e19\u0e35'), ('69', '\u0e2a\u0e38\u0e23\u0e34\u0e19\u0e17\u0e23\u0e4c'), ('70', '\u0e2b\u0e19\u0e2d\u0e07\u0e04\u0e32\u0e22'), ('71', '\u0e2b\u0e19\u0e2d\u0e07\u0e1a\u0e31\u0e27\u0e25\u0e33\u0e20\u0e39'), ('72', '\u0e2d\u0e48\u0e32\u0e07\u0e17\u0e2d\u0e07'), ('73', '\u0e2d\u0e38\u0e14\u0e23\u0e18\u0e32\u0e19\u0e35'), ('74', '\u0e2d\u0e38\u0e17\u0e31\u0e22\u0e18\u0e32\u0e19\u0e35'), ('75', '\u0e2d\u0e38\u0e15\u0e23\u0e14\u0e34\u0e15\u0e16\u0e4c'), ('76', '\u0e2d\u0e38\u0e1a\u0e25\u0e23\u0e32\u0e0a\u0e18\u0e32\u0e19\u0e35'), ('77', '\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e40\u0e08\u0e23\u0e34\u0e0d')], max_length=20, null=True)),
                ('customer_postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('customer_typeofphone', models.CharField(blank=True, choices=[('1', 'IOS'), ('2', 'Android')], max_length=7, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status_payment', models.CharField(choices=[('1', 'Waiting Payment'), ('2', 'Paid'), ('3', 'Report'), ('4', 'Close')], default='1', max_length=20)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_owner', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_target', models.CharField(blank=True, choices=[('1', 'SCB'), ('2', 'KTB')], max_length=20, null=True)),
                ('payment_time', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=50)),
                ('bill_image', models.ImageField(upload_to='bill_images')),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_phonenumber', models.CharField(blank=True, max_length=10, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('product_quantity', models.CharField(max_length=3)),
                ('product_detail', models.CharField(max_length=200)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalprice_per_product', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_report', models.CharField(max_length=200)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='productinorder_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.ProductInOrder'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer'),
        ),
    ]
