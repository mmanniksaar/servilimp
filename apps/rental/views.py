from django.shortcuts import render, get_object_or_404
from apps.category.models import Category
from apps.rental.models import Product
from apps.carts.models import CartItem
from apps.carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404


def rental(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()

    context = {
        'products' : products,
        'product_count': product_count,
    }
    return render(request, 'rental.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)

        if request.user.is_authenticated:
            # Otsime toote kasutaja ostukorvist
            in_cart = CartItem.objects.filter(user=request.user, product=single_product).exists()
        else:
            # Otsime toote anonüümsest ostukorvist (kasutades session cart_id)
            in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Product.DoesNotExist:
        return redirect('home')  # Suunatakse avalehele, kui toodet pole
    except Exception as e:
        print(f"Viga product_detail vaates: {e}")

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'product_detail.html', context)
