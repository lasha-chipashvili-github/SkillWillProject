from django.contrib import admin

from .models import (
    Product, ProductCategory, Size, Colour, Brand, Item
)

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product_category", "product_brand", "product_name", )}

admin.site.register(Product, ProductAdmin)


class ItemAdimn(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product", "size", "colour",)}

admin.site.register(Item, ItemAdimn)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand_name",)}

admin.site.register(Brand, BrandAdmin)

class SizeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("size",)}

admin.site.register(Size, SizeAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product_category",)}

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ColourAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("colour",)}

admin.site.register(Colour, ColourAdmin)

