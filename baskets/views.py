from django.shortcuts import redirect
from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response

from accounts.models import CustomUser
from products.models import Item
from .models import Basket, Favorite
from .serializers import BasketSerializer, BasketPUTSerializer, FavoriteSerializer


class BasketListView(generics.ListAPIView):
    serializer_class = BasketSerializer

    def get_queryset(self):
        owner = self.request.user
        return Basket.objects.filter(owner=owner)


class BasketCreateView(generics.CreateAPIView):
    serializer_class = BasketPUTSerializer
    queryset = Basket.objects.all()

    def perform_create(self, serializer):
        item_id = int(self.request.POST.get('item'))
        amount = int(self.request.POST.get('amount'))

        item = Item.objects.get(pk=item_id)
        owner_id = self.request.user.id
        owner = CustomUser.objects.get(pk=owner_id)

        if item.stock >= amount:
            basket = Basket(owner=owner, item=item, amount=amount)
            basket.save()
            item.stock -= amount
            if item.stock > 1:
                item.save()
            else:
                item.is_available = False

        else:
            return Response("მარაგში მოთხოვნილი რაოდენობის ნივთი არ არის."
                            "დარჩენილია მხოლოდ {item.stock} ნივთი", status=status.HTTP_400_BAD_REQUEST)





class BasketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    # http_method_names = მეთოდების დაშვება



class FavoriteListView(generics.ListAPIView):
    class Meta:
        model = Favorite
        serializer_class = FavoriteSerializer
        permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(user=user)

class FavoriteDetaliView(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Favorite
        serializer_class = FavoriteSerializer
        permission_classes = [permissions.IsAuthenticated]








