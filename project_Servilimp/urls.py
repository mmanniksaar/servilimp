from django.contrib import admin
from django.urls import path, include
from . import views
from apps.clients.views import clients_view
from apps.gallery.views import gallery_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),        # '' tähendab, et tegemist on esilehega- home.html, index.html jne.
   # path('rental/', views.rental, name='rental'), 
    path('services/', views.services, name='services'),
    path('contact/', views.contact_view, name='contact'),
    path('admin/', admin.site.urls),
    #path('admin/defender/', include('defender.urls')),  # defender admin
    path('clients/', include('apps.clients.urls')),        # 'clients/' clients.urls suunab faili clients/urls.py
    path('gallery/', include('apps.gallery.urls')),        # 'gallery/' gallery.urls suunab faili gallery/urls.py
    path('rental/', include('apps.rental.urls')),  
    path('about/', include('apps.about.urls')),        # 'abouts/' abouts.urls suunab faili clients/urls.py
 
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)