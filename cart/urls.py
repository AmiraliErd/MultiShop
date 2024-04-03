from django.urls import path
from .views import CartDetailView, CartAddView, CartDeleteView, OrderDetailView, OrderCreationView, ApplyDiscountView, \
    SendRequestView, VerifyView


app_name = 'cart'
urlpatterns = [
    path('detail', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>', CartAddView.as_view(), name='cart_add'),
    path('delete/<str:id>', CartDeleteView.as_view(), name='cart_delete'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('order/add', OrderCreationView.as_view(), name='order_creation'),
    path('applydiscount/<int:pk>', ApplyDiscountView.as_view(), name='apply_discount'),
    path('sendrequest/<int:pk>', SendRequestView.as_view(), name='send_request'),
    path('verify/', VerifyView.as_view(), name='verify_request'),
]
