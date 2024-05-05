from cart.cart_module import Cart
from product.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from cart.models import Order
from django.shortcuts import get_object_or_404


def cart_counter(request):
    cart = Cart(request)
    counter = cart.count()
    categories = Category.objects.all()
    return {'counter': counter, 'categories': categories}


# def navbar(request):
#     categories = Category.objects.all()
#     return {'categories': categories}
