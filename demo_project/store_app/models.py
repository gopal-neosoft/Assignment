# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import os
# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    parent_id = models.ForeignKey('self', related_name='parentId', null=True, blank=True, verbose_name='Parent Category')
    created_by = models.ForeignKey(User, related_name='creator', blank=True)
    created_date = models.DateField(auto_now_add=True, editable=False, null=True, blank=True)
    modify_by = models.ForeignKey(User, related_name='modifier', null=True, blank=True)
    modified_date = models.DateField(editable=False, null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    sku = models.CharField(max_length=45, null=True, blank=True)
    short_description = models.CharField(max_length=100, null=True, blank=True)
    long_description = models.TextField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    special_price = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    special_price_from = models.DateField(null=True, blank=True)
    special_price_to = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)
    quantity = models.IntegerField(null=True, blank=True)
    meta_title = models.CharField(max_length=25, null=True, blank=True)
    meta_description = models.TextField(max_length=200, null=True, blank=True)
    meta_keywords = models.TextField(max_length=200, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='creator1', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, editable=False, null=True, blank=True)
    modify_by = models.ForeignKey(User, related_name='modifier1', null=True, blank=True)
    modified_date = models.DateField(editable=False, null=True, blank=True)
    is_featured = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    product_image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)
    modify_by = models.IntegerField(null=True, blank=True)
    modify_date = models.DateField(null=True, blank=True)
    product = models.ForeignKey(Product, null=True, related_name='image')
    images = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Product Images'

    def image_tag(self):
        return mark_safe('<img src="/media/%s" alt="img" />' % self.images)
