from django.shortcuts import render, redirect, get_object_or_404
from apps.rental.models import Product
from apps.order.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

# session cart id
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

# add product in cart (product_id)
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id) # get the product by id
    #if request.method == 'POST':
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1 # cart_item.quantity = cart_item.quantity +1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')


def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)  # get the product
    # If the user is authenticated
    if current_user.is_authenticated:
        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, user=current_user)
        else:
            cart_item = CartItem.objects.create(product=product, quantity=1, user=current_user, )
            cart_item.save()
        return redirect('cart')
    # If the user is not authenticated
    else:

        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))  # get the cart using the cart_id present in the session
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, cart=cart)
        else:
            cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart, )
            cart_item.save()
        return redirect('cart')

# remove product in cart
def remove_to_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

# remove item in cart
def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request)) #get cart item session id
    product = get_object_or_404(Product, id=product_id) # get product id
    cart_item = CartItem.objects.get(product=product, cart=cart) # cart item
    cart_item.delete() # delete item
    return redirect('cart')

# cart context
def cart(request, total = 0, quantity=0, cart_items=None ):

     try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (24 * total)/100
        grand_total = total + tax

     except ObjectDoesNotExist: # do nothing if obj not exist
         pass

     context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
        'tax' : tax,
        'grand_total' : grand_total,
     }
     return render(request, 'order.html', context)

@login_required(login_url="login")
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (24 * total) / 100
        grand_total = total + tax

    except ObjectDoesNotExist:  # do nothing if obj not exist
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/checkout.html', context)