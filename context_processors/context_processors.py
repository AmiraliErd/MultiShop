from cart.cart_module import Cart


def cart_counter(request):
    cart = Cart(request)
    counter = cart.count()

    return {'counter': counter}
