# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Product, ProductImages
import datetime

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'created_by', 'created_date', 'modified_date', 'status')
    exclude = ('modify_by', 'created_date', 'modified_date', 'created_by')

    class Meta:
        model = Category

    def save_model(self, request, obj, form, change):
        if change:
            obj.modify_by = request.user
            obj.modified_date = datetime.datetime.now()
        else:
            obj.created_by = request.user
            obj.created_date = datetime.datetime.now()
        obj.save()

    def parent_category(self, obj):
        return obj.parent_id


admin.site.register(Category, CategoryAdmin)


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    fields = ('images', 'image_tag', )
    readonly_fields = ('image_tag',)
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'short_description', 'long_description', 'price', 'special_price', 'special_price_from', 'special_price_to', 'status', 'quantity', 'meta_title', 'meta_description', 'meta_keywords', 'is_featured')
    exclude = ('created_by', 'modify_by', 'created_date', 'modified_date', 'product_image')
    inlines = [ProductImagesInline, ]

    class Meta:
        model = Product

    def save_model(self, request, obj, form, change):
        if change:
            obj.modify_by = request.user
            obj.modified_date = datetime.datetime.now()
            obj.product_image = request.user
        else:
            obj.created_by = request.user
            obj.created_date = datetime.datetime.now()
        obj.save()


admin.site.register(Product, ProductAdmin)




