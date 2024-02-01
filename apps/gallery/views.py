from django.shortcuts import render, get_object_or_404
from .models import Gallery


""" def gallery_view(request):
    gallery_items = Gallery.objects.all()
    
    context = {}
    context['gallery_items'] = gallery_items
    context['meta'] = gallery_items.as_meta()
    
  #  context = {
  #      'gallery_items': gallery_items,
  #  }
    return render(request, 'gallery.html' ,context) """
    
from django.shortcuts import render
from .models import Gallery
from meta.views import Meta

def gallery_view(request):
    gallery_items = Gallery.objects.all()

    # Loome Meta objekti ja määrame sellele vastavad väärtused
    meta = Meta()
    meta.use_facebook = True  # Muuda vastavalt vajadusele
    meta.use_twitter = True   # Muuda vastavalt vajadusele

    # Kui teil on vaja seada OpenGraph andmed
    if gallery_items.exists():
        first_gallery = gallery_items.first()
        meta.title = first_gallery.name
        meta.description = first_gallery.description
        meta.image = request.build_absolute_uri(first_gallery.gallery_image.url)

    context = {
        'gallery_items': gallery_items,
        'meta': meta,
    }
    
    return render(request, 'gallery.html', context)
