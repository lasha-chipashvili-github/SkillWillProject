from django.urls import path

from .views import ProductList, ProductView, ItemView, ItemList

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<slug:slug>/', ProductView.as_view(), name='product_detail'),
    path('<slug:slug>/items/', ItemList.as_view(), name='item_list'),
    path('items/<slug:slug>/', ItemView.as_view(), name='item_detail'),
]
