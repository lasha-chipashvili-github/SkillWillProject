from rest_framework import serializers

from .models import ProductCategory, Size,  Brand, Colour, Product, Item

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'product_category',
            'parent_category_id',
            'slug'
        )


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            'id',
            'size',
            'slug',
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'brand_name',
            'slug',
        )




class ColourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colour
        fields = (
            'id',
            'colour',
            'slug',
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        models = Product
        fields = (
            'id',
            'product_name',
            'product_description',
            'product_category',
            'slug',
        )

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        models = Item
        fields = (
            'id',
            'product',
            'size',
            'colour',
            'date_of_addition',
            'price',
            'is_available'
        )

