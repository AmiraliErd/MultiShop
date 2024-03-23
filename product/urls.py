from django.urls import path
from .views import ProductDetailView


app_name = 'product'
urlpatterns = [
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail')
]