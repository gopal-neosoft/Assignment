# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0014_auto_20171018_0615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='sub_category',
            new_name='parent_id',
        ),
    ]
