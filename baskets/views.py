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


        # if item.stock >= amount:
        #     print("it's more")
        #     basket, created = Basket.objects.get_or_create(owner=owner, item=item)
        #     ("it's error")
        #     if not created:
        #         print("not created")
        #
        #         item.stock -= amount
        #         print(f"stock = {item.stock}")
        #         item.save()
        #         print("stock decreased")
        #         serializer.save()
        #         print("basket saved")
        #         return redirect('basket_list')
        #
        #     else:
        #         print("created")
        #         Basket.objects.create(owner=owner, item=item, amount=amount)
        #
        #     serializer.save(basket=basket)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)




class BasketDetailView(generics.RetrieveUpdateDestroyAPIView):
    pass

