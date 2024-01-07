from django.contrib import admin
from django.urls import path, include
from . import views
from clients.views import clients_view
from gallery.views import gallery_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),        # '' tähendab, et tegemist on esilehega- home.html, index.html jne.
    path('about/', views.about, name='about'), 
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('clients/', views.clients, name='clients'),
    path('admin/', admin.site.urls),
    path('admin/defender/', include('defender.urls')),  # defender admin
    path('clients/', include('clients.urls')),        # 'clients/' clients.urls suunab faili clients/urls.py
    path('gallery/', include('gallery.urls')),        # 'gallery/' gallery.urls suunab faili gallery/urls.py
  #  path('cart/', include('carts.urls')),
  #  path('accounts/', include('accounts.urls')),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)