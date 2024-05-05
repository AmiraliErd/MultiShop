from django.urls import path
from .views import ProductDetailView, NavbarPartialView, CategoryStyle, ProductsListView, search


app_name = 'product'
urlpatterns = [
    path('all', ProductsListView.as_view(), name='products_list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('navbar', NavbarPartialView.as_view(), name='navbar'),
    path('category', CategoryStyle.as_view(), name='category'),
    path('search/', search, name='search'),
]