from django.shortcuts import render, redirect, get_object_or_404
from apps.rental.models import Product
from apps.carts.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db import connection
from decimal import Decimal

def ensure_db_connection():
    try:
        if not connection.is_usable():
            connection.close()
            connection.connect()
    except Exception as e:
        print("Database Connection Error:", e)


# ✅ Abifunktsioon: loob või tagastab sessioonipõhise ostukorvi ID
def _cart_id(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


# ✅ Lisab toote ostukorvi
def add_to_cart(request, product_id):
    ensure_db_connection()
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            user=request.user,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        cart, _ = Cart.objects.get_or_create(cart_id=_cart_id(request))
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            cart=cart,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('cart')


# ✅ Eemaldab 1 ühiku tootest ostukorvist
def remove_to_cart(request, product_id):
    ensure_db_connection()
    product = get_object_or_404(Product, id=product_id)

    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    except CartItem.DoesNotExist:
        pass

    return redirect('cart')


# ✅ Eemaldab toote ostukorvist
def remove_cart_item(request, product_id):
    ensure_db_connection()
    product = get_object_or_404(Product, id=product_id)

    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart)

        cart_item.delete()

    except CartItem.DoesNotExist:
        pass

    return redirect('cart')


# ✅ Ostukorvi vaade
def cart(request, total=0, quantity=0, cart_items=None):
    ensure_db_connection()
    try:
        tax = 0
        grand_total = 0
        in_cart = False  # Algväärtus

        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
            in_cart = cart_items.exists()  # Kas vähemalt üks toode on ostukorvis?
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            in_cart = cart_items.exists()

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (24 * total) / 100
        grand_total = total + Decimal(tax)

    except ObjectDoesNotExist:
        pass  # Kui ostukorvi pole, siis pole ka tooteid

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
        'in_cart': in_cart,  # Lisame selle väärtuse
    }

    return render(request, 'cart.html', context)



# ✅ Seob anonüümse ostukorvi sisseloginud kasutajaga
@login_required(login_url="login")
def merge_cart_with_user(request):
    ensure_db_connection()
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        return redirect('cart')

    user_cart, created = Cart.objects.get_or_create(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart)

    for item in cart_items:
        existing_item = CartItem.objects.filter(user=request.user, product=item.product).first()
        if existing_item:
            existing_item.quantity += item.quantity
            existing_item.save()
        else:
            item.user = request.user
            item.cart = user_cart
            item.save()

    cart.delete()
    return redirect('cart')


# ✅ Kassaleht, ühendab anonüümse ostukorvi kasutajaga
@login_required(login_url="login")
def checkout(request):
    ensure_db_connection()
    merge_cart_with_user(request)  # ✅ Enne checkouti ühendame ostukorvid
    cart_items = CartItem.objects.filter(user=request.user, is_active=True)

    total = sum(item.product.price * item.quantity for item in cart_items)
    tax = float(total) * 0.24
    grand_total = total + Decimal(tax)
    context = {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'checkout.html', context)

