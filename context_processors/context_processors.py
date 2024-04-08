from cart.cart_module import Cart
from product.models import Category


def cart_counter(request):
    cart = Cart(request)
    counter = cart.count()
    categories = Category.objects.all()
    return {'counter': counter, 'categories': categories}


# def navbar(request):
#     categories = Category.objects.all()
#     return {'categories': categories}


