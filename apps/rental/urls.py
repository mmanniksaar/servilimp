from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.rental, name='rental'),
    path('category/<slug:category_slug>/', views.rental, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

    #path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

]

