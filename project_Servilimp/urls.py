from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', views.home, name='home'),        # '' tähendab, et tegemist on esilehega- home.html, index.html jne.
   # path('about/', views.about, name='about'), 
   # path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('cleaning/', views.cleaning, name='cleaning'),
    path('admin/', admin.site.urls),
    #path('admin/defender/', include('defender.urls')),  # defender admin
    path('clients/', include('apps.clients.urls')),        # 'clients/' clients.urls suunab faili clients/urls.py
    #path('contact/', include('apps.contact.urls')),
    #path('order/', include('apps.order.urls')),
    path('about/', include('apps.about.urls')),
    path('cart/', include('apps.carts.urls')),
    path('rental/', include('apps.rental.urls')),
    #path('sentry-debug/', trigger_error),
    path('accounts/', include('apps.accounts.urls')),

    path('gallery/', include('apps.gallery.urls')),        # 'gallery/' gallery.urls suunab faili gallery/urls.py
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)