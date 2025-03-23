from django.db import connection
from apps.carts.models import CartItem, Cart

def counter(request):
    try:
        if not connection.is_usable():
            connection.close()
            connection.connect()

        cart_count = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.filter(cart_id=request.session.session_key).first()
            cart_items = CartItem.objects.filter(cart=cart, is_active=True) if cart else []

        for cart_item in cart_items:
            cart_count += cart_item.quantity

    except Exception as e:
        print("Cart Counter Error:", e)
        cart_count = 0  # Väldi serveri crash'i

    return dict(cart_count=cart_count)
