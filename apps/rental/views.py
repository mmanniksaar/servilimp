from django.shortcuts import render, get_object_or_404
from apps.category.models import Category
from apps.rental.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404


def rental_view(request, category_slug=None):
    products = None
    product_count = 0

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }

    return render(request, 'rental.html', context)
