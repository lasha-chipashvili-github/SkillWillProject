from rest_framework import serializers

from products.models import Item
from .models import Basket, Favorite
from dj_rest_auth.serializers import UserDetailsSerializer


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

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = [
            'user',
            'product'
        ]
