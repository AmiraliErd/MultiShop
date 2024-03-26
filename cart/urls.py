from django.urls import path
from .views import CartDetailView, CartAddView, CartDeleteView


app_name = 'cart'
urlpatterns = [
    path('detail', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>', CartAddView.as_view(), name='cart_add'),
    path('delete/<str:id>', CartDeleteView.as_view(), name='cart_delete'),
]
