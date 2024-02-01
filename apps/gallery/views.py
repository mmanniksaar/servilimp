from django.shortcuts import render, get_object_or_404
from .models import Gallery


""" def gallery_view(request):
    gallery_items = Gallery.objects.all()
    
    context = {
        'gallery_items': gallery_items,
    }
    return render(request, 'gallery.html' ,context) """


def gallery_view(request, id):
    template = 'gallery.html'
    gallery_items = Gallery.objects.get(pk=id)
    context = {}
    context['gallery_items'] = gallery_items
    context['meta'] = gallery_items.as_meta()
    return render(request, template, context)