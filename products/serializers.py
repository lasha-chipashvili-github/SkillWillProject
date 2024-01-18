from rest_framework import serializers

from .models import ProductCategory, Size, Brand, Colour, Product, Item, ProductImage


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


class ProductImageSerializer(serializers.ModelSerializer):
    files = serializers.FileField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = ProductImage
        fields = ['files']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    # uploaded_images = serializers.ListField(
    #     child=serializers.ImageField(allow_empty_file=False, use_url=False),
    #     write_only=True
    # )

    class Meta:
        model = Product
        fields = (
            'id',
            'product_name',
            'product_description',
            'product_category',
            'prod_slug',
            'prod_price',
            'images',
            # 'uploaded_images'
        )
        depth = 10

    # def create(self, validated_data):
    #     uploaded_images = validated_data.pop("uploaded_images")
    #     product = Product.objects.create(**validated_data)
    #
    #     for image in uploaded_images:
    #         ProductImage.objects.create(product=product, files=image)
    #
    #     return product

class ItemSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(source="product.prod_price", max_digits=7, decimal_places=2)

    class Meta:
        model = Item
        fields = (
            'id',
            'product',
            'size',
            'colour',
            'date_of_addition',
            'price',
            'stock',
            'is_available',
            'itm_slug'
        )
        depth = 10
        lookup_field = 'itm_slug'
