from rest_framework import generics

from .models import (
    Item,
    Product,
    ProductCategory,
    Size,
    Brand,
    Colour,
)
from .serializers import (
    ItemSerializer,
    ProductSerializer,
    ProductCategorySerializer,
    SizeSerializer,
    BrandSerializer,
    ColourSerializer,
)


# Create your views here.

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
