from django.contrib import admin
from .models import Product, Category, ProductStatus
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'old_price',
        'price',
        'rating',
        'product_status',
        'featured',
        'promotion',
    )
    summernote_fields = ('description, product_details,  features')
    ordering = ('sku',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(ProductStatus)
class ProductStatusAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
