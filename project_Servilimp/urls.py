from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from apps.gallery.models import Gallery
from apps.rental.models import Product
from apps.clients.models import Client
from apps.about.models import About
from apps.category.models import Category
from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

""" info_dict = {
    "queryset_gallery": Gallery.objects.all(),
    "date_field": "pub_date",
    "queryset_rental": Product.objects.all(),
    "date_field": "pub_date",
    "queryset_clients": Client.objects.all(),
    "date_field": "pub_date",
    "queryset_about": About.objects.all(),
    "date_field": "pub_date",
} """


urlpatterns = [
    path('', views.home, name='home'),        # '' tähendab, et tegemist on esilehega- home.html, index.html jne.
    path('cleaning/', views.cleaning, name='cleaning'),
    path('contact/', views.contact_view, name='contact'),
    path('admin/', admin.site.urls),
    #path('admin/defender/', include('defender.urls')),  # defender admin
    path('clients/', include('apps.clients.urls')),        # 'clients/' clients.urls suunab faili clients/urls.py
    path('gallery/', include('apps.gallery.urls')),        # 'gallery/' gallery.urls suunab faili gallery/urls.py
    path('rental/', include('apps.rental.urls')),  
    path('about/', include('apps.about.urls')),        # 'abouts/' abouts.urls suunab faili clients/urls.py

    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),
 
 
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)