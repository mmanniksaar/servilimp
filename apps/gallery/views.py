from django.shortcuts import render, get_object_or_404
from .models import Gallery


def gallery_view(request):
    gallery_items = Gallery.objects.all()
    
    context = {
        'gallery_items': gallery_items,
    }
    return render(request, 'gallery.html' ,context)


