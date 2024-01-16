from django.http import JsonResponse
from django.views.generic import DetailView
from rest_framework import generics, viewsets
from django.views import generic
from rest_framework.views import Response

from .models import (
    Item,
    Product,
    ProductCategory,
    Size,
    Brand,
    Colour,
    ProductImage,
)
from .serializers import (
    ItemSerializer,
    ProductSerializer,
    ProductCategorySerializer,
    SizeSerializer,
    BrandSerializer,
    ColourSerializer,
    ProductImageSerializer,
)


# Create your views here.

class ProductList(generics.ListAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []  # disables permission

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

class ItemList(generics.ListAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = []  # disables permission

    # queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        product_slug = self.kwargs['slug']
        product_id = Product.objects.get(slug=product_slug)
        queryset = Item.objects.filter(product_id=product_id)
        return queryset



class ItemView(generics.RetrieveAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    queryset = Item.objects.filter(is_available=True)
    serializer_class = ItemSerializer
    lookup_field = 'slug'







