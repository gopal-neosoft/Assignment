# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0028_auto_20171023_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='product_id',
        ),
        migrations.AddField(
            model_name='productimages',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='store_app.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='created_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='modify_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='modify_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
