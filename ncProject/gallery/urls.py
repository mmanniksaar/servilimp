
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('gallery/', views.gallery_view, name='gallery'),
]

