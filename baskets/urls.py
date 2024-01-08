from django.urls import path

from .views import BasketListView, BasketDetailView, BasketCreateView

urlpatterns = [
    path('', BasketListView.as_view(), name='basket_list'),
    path('add/', BasketCreateView.as_view(), name='basket_add'),
    path('<int:pk>/', BasketDetailView.as_view(), name='basket_detail'),
]