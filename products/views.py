from django.http import JsonResponse
from django.views.generic import DetailView
from rest_framework import generics, viewsets
from django.views import generic
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework import filters

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

    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'product_description']


class ProductView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []  # disables permission

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'prod_slug'

class ItemList(generics.ListAPIView):
    authentication_classes = [] # disables authentication
    permission_classes = []  # disables permission

    # queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        product_slug = self.kwargs['prod_slug']
        product_id = Product.objects.get(prod_slug=product_slug)
        queryset = Item.objects.filter(product_id=product_id)
        return queryset



class ItemView(generics.RetrieveAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    queryset = Item.objects.filter(is_available=True)
    serializer_class = ItemSerializer
    lookup_field = 'id'

