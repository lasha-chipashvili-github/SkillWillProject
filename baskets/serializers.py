from rest_framework import serializers

from products.models import Item
from .models import Basket


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
                'id',
                'owner',
                'item',
                'amount',
                'total_price',
                'date_created',
                'date_modified'
                  ]

class BasketPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
                'id',
                'owner',
                'item',
                'amount',
                'date_created',
                'date_modified'
                  ]

