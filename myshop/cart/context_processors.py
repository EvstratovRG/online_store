from .cart import Cart

# контекстный процессор


def cart(request):
    return {'cart': Cart(request)}
