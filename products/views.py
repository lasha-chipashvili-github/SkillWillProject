from django.http import JsonResponse
from django.views.generic import DetailView
from rest_framework import generics, viewsets
from django.views import generic

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
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ItemList(generics.ListAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemView(generics.RetrieveAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    queryset = Item.objects.filter(is_available=True)
    serializer_class = ItemSerializer
    lookup_field = 'slug'







