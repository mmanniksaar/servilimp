from django.shortcuts import render, get_object_or_404
from apps.category.models import Category
from apps.rental.models import Product
from apps.order.models import CartItem
from apps.order.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404


def rental_view(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')



    context = {
        'products': products,
    }

    return render(request, 'rental1.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id= _cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart'   : in_cart,
    }
    return render(request, 'product_detail.html', context)