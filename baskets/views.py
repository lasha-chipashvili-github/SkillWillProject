from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response

from accounts.models import CustomUser
from products.models import Item
from .models import Basket
from .serializers import BasketSerializer, BasketPUTSerializer


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
        owner_id = int(self.request.POST.get('owner'))
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






