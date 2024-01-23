from django.shortcuts import render, get_object_or_404
#from .models import Gallery
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404


""" def rental_view(request):
    gallery_items = Gallery.objects.all()
    context = {
        'gallery_items': gallery_items,
    }
    print(gallery_items)
    return render(request, 'gallery.html' ,context) """


def rental_view(request):
  template = loader.get_template('rental.html')
  return HttpResponse(template.render())