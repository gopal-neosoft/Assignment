# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 14:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0009_auto_20171013_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='modify_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
