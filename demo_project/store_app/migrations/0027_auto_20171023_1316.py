# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0026_auto_20171023_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='webwerks/demo_project/photos/'),
        ),
    ]
