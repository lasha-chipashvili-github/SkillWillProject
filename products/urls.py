from django.urls import path

from .views import ProductList, ProductView, ItemView, ItemList, ProductDetailView

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<slug:prod_slug>/', ProductView.as_view(), name='product_detail'),
    path('<slug:prod_slug>/items/', ItemList.as_view(), name='item_list'),
    path('<slug:prod_slug>/items/<int:id>/', ItemView.as_view(), name='item_detail'),
]
