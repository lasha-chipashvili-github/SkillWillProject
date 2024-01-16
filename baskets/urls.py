from django.urls import path

from .views import BasketListView, BasketDetailView, BasketCreateView, FavoriteListView, FavoriteDetaliView

urlpatterns = [
    path('', BasketListView.as_view(), name='basket_list'),
    path('add/', BasketCreateView.as_view(), name='basket_add'),
    path('<int:pk>/', BasketDetailView.as_view(), name='basket_detail'),
    path('favorites/', FavoriteListView.as_view(), name='favorite_products'),
    path('favorites/<int:pk>/', FavoriteDetaliView.as_view(), name='favorite_product')
]