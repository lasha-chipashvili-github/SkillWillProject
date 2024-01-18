from drf_spectacular.utils import extend_schema
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.schemas import AutoSchema


from .models import (
    Item,
    Product,
    # ProductCategory,
    # Size,
    # Brand,
    # Colour,
    # ProductImage,
)
from .serializers import (
    ItemSerializer,
    ProductSerializer,
    # ProductCategorySerializer,
    # SizeSerializer,
    # BrandSerializer,
    # ColourSerializer,
    # ProductImageSerializer,
)


# Create your views here.

class ProductList(generics.ListAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    parser_class = [MultiPartParser, FormParser]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'product_description']


class ProductView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []  # disables permission


    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'prod_slug'


class ProductDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

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






# @api_view(['GET'])
# def get_product_sizes(request, prod_slug):
#     product = Product.objects.get(prod_slug=prod_slug)
#     items = Item.objects.filter(product_id=product.id)
#     sizes = []
#     amount = []
#     for item in items:
#         if item.is_available:
#             sizes.append(item.size.size)
#             amount.append(item.stock)
#     lst = {sizes[i]: amount[i] for i in range(len(sizes))}
#     return Response(lst, status=status.HTTP_200_OK)





@api_view(['GET'])
def get_product_sizes(request, prod_slug):
    product = Product.objects.get(prod_slug=prod_slug)
    items = Item.objects.filter(product_id=product.id, is_available=True)

    # Use a serializer to define the response schema
    serializer = ItemSerializer(items, many=True)
    serialized_data = serializer.data

    # If you want to customize the response format, you can do it here
    response_data = {item['size']['size']: item['stock'] for item in serialized_data}

    return Response(response_data)

