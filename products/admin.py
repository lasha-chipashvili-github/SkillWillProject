from django.contrib import admin

from .models import (
    Product, ProductCategory, Size, Colour, Brand, Item
)

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Size)
admin.site.register(Colour)
admin.site.register(Brand)
admin.site.register(Item)