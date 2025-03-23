from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from apps.rental.models import Product

""" def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def services(request):
  template = loader.get_template('services.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def clients(request):
  template = loader.get_template('clients.html')
  return HttpResponse(template.render())

def gallery(request):
  template = loader.get_template('gallery.html')
  return HttpResponse(template.render())

def rental(request):
  template = loader.get_template('rental.html')
  return HttpResponse(template.render())
 """

def home(request):
    products = Product.objects.all().filter(is_available= True)
    context = {
        'products': products,
    }
    return render(request, 'home.html',context)

def contact(request):
    return render(request, 'contact.html')

def cleaning(request):
    return render(request, 'cleaning.html')
