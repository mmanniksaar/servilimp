from django.shortcuts import render, get_object_or_404
from apps.category.models import Category
from apps.rental.models import Product
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
