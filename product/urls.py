from django.urls import path
from .views import ProductDetailView, NavbarPartialView, CategoryStyle


app_name = 'product'
urlpatterns = [
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('navbar', NavbarPartialView.as_view(), name='navbar'),
    path('category', CategoryStyle.as_view(), name='category'),
]