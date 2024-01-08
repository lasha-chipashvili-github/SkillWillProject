from django.urls import path

from .views import ProductList, ItemView, ItemList

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('product=<slug:slug>/', ItemView.as_view(), name='product_detail'),
    path('items/', ItemList.as_view(), name='item_list'),

]